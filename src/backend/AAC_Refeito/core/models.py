from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Usuario(AbstractUser):
    class Perfil(models.TextChoices):
        ALUNO = "ALUNO", "Aluno"
        COORDENADOR = "COORDENADOR", "Coordenador"
        ORG = "ORG", "Organização Acadêmica"

    perfil = models.CharField(
        max_length=20,
        choices=Perfil.choices,
        default=Perfil.ALUNO
    )

    def __str__(self):
        return self.username


class Aluno(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="aluno"
    )
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    semestre_ingresso = models.IntegerField(validators=[MinValueValidator(1)])
    total_horas_integralizadas = models.IntegerField(default=0)

    def atualizar_total_horas(self):
        total = self.atividades.filter(
            status=AtividadeComplementar.Status.APROVADO
        ).aggregate(
            total=models.Sum("carga_horaria_validada")
        )["total"] or 0

        self.total_horas_integralizadas = total
        self.save(update_fields=["total_horas_integralizadas"])
        return total

    def __str__(self):
        return f"{self.usuario.username} - {self.matricula}"


class Coordenador(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="coordenador"
    )
    sia_funcionario = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.usuario.username


class OrgAcademica(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="organizacao"
    )
    nome_entidade = models.CharField(max_length=100)
    cargo_representante = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_entidade


class EixoTematico(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class TipoAtividade(models.Model):
    nome = models.CharField(max_length=100)
    limite_horas_total = models.IntegerField(validators=[MinValueValidator(1)])
    limite_horas_por_evento = models.IntegerField(validators=[MinValueValidator(1)])
    eixo_tematico = models.ForeignKey(
        EixoTematico,
        on_delete=models.CASCADE,
        related_name="tipos_atividade"
    )

    class Meta:
        verbose_name = "Tipo de Atividade"
        verbose_name_plural = "Tipos de Atividade"
        unique_together = ("nome", "eixo_tematico")

    def __str__(self):
        return self.nome


class AtividadeComplementar(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        APROVADO = "APROVADO", "Aprovado"
        REPROVADO = "REPROVADO", "Reprovado"

    class Origem(models.TextChoices):
        INTERNA = "INTERNA", "Interna"
        EXTERNA = "EXTERNA", "Externa"

    descricao = models.TextField()
    data_realizacao = models.DateField(null=True, blank=True)
    carga_horaria_solicitada = models.IntegerField(validators=[MinValueValidator(1)])
    carga_horaria_validada = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE
    )
    tipo_origem = models.CharField(
        max_length=20,
        choices=Origem.choices,
        default=Origem.EXTERNA
    )
    caminho_comprovante = models.FileField(
        upload_to="comprovantes/",
        null=True,
        blank=True
    )
    feedback = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="atividades"
    )
    coordenador = models.ForeignKey(
        Coordenador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="atividades_analisadas"
    )
    organizacao = models.ForeignKey(
        OrgAcademica,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="atividades_lancadas"
    )
    tipo_atividade = models.ForeignKey(
        TipoAtividade,
        on_delete=models.CASCADE,
        related_name="atividades"
    )

    class Meta:
        verbose_name = "Atividade Complementar"
        verbose_name_plural = "Atividades Complementares"
        ordering = ["-criado_em"]

    def aprovar(self, coordenador, carga_horaria_validada=None, justificativa=""):
        horas = carga_horaria_validada or self.carga_horaria_solicitada
        limite_evento = self.tipo_atividade.limite_horas_por_evento

        if horas > limite_evento:
            horas = limite_evento

        self.status = self.Status.APROVADO
        self.coordenador = coordenador
        self.carga_horaria_validada = horas
        self.feedback = justificativa
        self.save()

        Validacao.objects.update_or_create(
            atividade=self,
            defaults={
                "coordenador": coordenador,
                "resultado": Validacao.Resultado.APROVADO,
                "carga_horaria_validada": horas,
                "justificativa": justificativa or "Atividade aprovada."
            }
        )

        self.aluno.atualizar_total_horas()

    def reprovar(self, coordenador, justificativa):
        self.status = self.Status.REPROVADO
        self.coordenador = coordenador
        self.carga_horaria_validada = 0
        self.feedback = justificativa
        self.save()

        Validacao.objects.update_or_create(
            atividade=self,
            defaults={
                "coordenador": coordenador,
                "resultado": Validacao.Resultado.REPROVADO,
                "carga_horaria_validada": 0,
                "justificativa": justificativa
            }
        )

        self.aluno.atualizar_total_horas()

    def __str__(self):
        return self.descricao[:60]


class Validacao(models.Model):
    class Resultado(models.TextChoices):
        APROVADO = "APROVADO", "Aprovado"
        REPROVADO = "REPROVADO", "Reprovado"

    atividade = models.OneToOneField(
        AtividadeComplementar,
        on_delete=models.CASCADE,
        related_name="validacao"
    )
    coordenador = models.ForeignKey(
        Coordenador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="validacoes"
    )
    resultado = models.CharField(
        max_length=20,
        choices=Resultado.choices
    )
    carga_horaria_validada = models.IntegerField(default=0)
    justificativa = models.TextField()
    data_analise = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Validação"
        verbose_name_plural = "Validações"
        ordering = ["-data_analise"]

    def __str__(self):
        return f"Validação #{self.id} - {self.resultado}"
