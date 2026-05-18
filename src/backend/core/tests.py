from django.test import TestCase

from .models import Usuario, Aluno, EixoTematico, TipoAtividade, AtividadeComplementar


class AtividadeComplementarTestCase(TestCase):
    def test_total_horas_aluno_soma_apenas_aprovadas(self):
        usuario = Usuario.objects.create_user(
            username="aluno",
            password="123456",
            perfil=Usuario.Perfil.ALUNO
        )
        aluno = Aluno.objects.create(
            usuario=usuario,
            matricula="20260001",
            curso="Engenharia de Software",
            semestre_ingresso=1
        )
        eixo = EixoTematico.objects.create(nome="Ensino")
        tipo = TipoAtividade.objects.create(
            nome="Curso",
            limite_horas_total=60,
            limite_horas_por_evento=30,
            eixo_tematico=eixo
        )

        AtividadeComplementar.objects.create(
            descricao="Curso Python",
            carga_horaria_solicitada=20,
            carga_horaria_validada=20,
            status=AtividadeComplementar.Status.APROVADO,
            tipo_origem=AtividadeComplementar.Origem.EXTERNA,
            aluno=aluno,
            tipo_atividade=tipo
        )

        self.assertEqual(aluno.atualizar_total_horas(), 20)
