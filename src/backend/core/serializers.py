from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import (
    Usuario,
    Aluno,
    Coordenador,
    OrgAcademica,
    EixoTematico,
    TipoAtividade,
    AtividadeComplementar,
    Validacao,
)


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "perfil", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for campo, valor in validated_data.items():
            setattr(instance, campo, valor)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AlunoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(perfil=Usuario.Perfil.ALUNO),
        source="usuario",
        write_only=True
    )

    class Meta:
        model = Aluno
        fields = "__all__"


class CoordenadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(perfil=Usuario.Perfil.COORDENADOR),
        source="usuario",
        write_only=True
    )

    class Meta:
        model = Coordenador
        fields = "__all__"


class OrgAcademicaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.filter(perfil=Usuario.Perfil.ORG),
        source="usuario",
        write_only=True
    )

    class Meta:
        model = OrgAcademica
        fields = "__all__"


class EixoTematicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EixoTematico
        fields = "__all__"


class TipoAtividadeSerializer(serializers.ModelSerializer):
    eixo_tematico = EixoTematicoSerializer(read_only=True)
    eixo_tematico_id = serializers.PrimaryKeyRelatedField(
        queryset=EixoTematico.objects.all(),
        source="eixo_tematico",
        write_only=True
    )

    class Meta:
        model = TipoAtividade
        fields = "__all__"


class AtividadeComplementarSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer(read_only=True)
    aluno_id = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(),
        source="aluno",
        write_only=True
    )

    coordenador = CoordenadorSerializer(read_only=True)
    coordenador_id = serializers.PrimaryKeyRelatedField(
        queryset=Coordenador.objects.all(),
        source="coordenador",
        write_only=True,
        required=False,
        allow_null=True
    )

    organizacao = OrgAcademicaSerializer(read_only=True)
    organizacao_id = serializers.PrimaryKeyRelatedField(
        queryset=OrgAcademica.objects.all(),
        source="organizacao",
        write_only=True,
        required=False,
        allow_null=True
    )

    tipo_atividade = TipoAtividadeSerializer(read_only=True)
    tipo_atividade_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoAtividade.objects.all(),
        source="tipo_atividade",
        write_only=True
    )

    percentual_conclusao = serializers.SerializerMethodField()

    class Meta:
        model = AtividadeComplementar
        fields = "__all__"
        read_only_fields = [
            "status",
            "carga_horaria_validada",
            "feedback",
            "criado_em",
            "atualizado_em",
        ]

    def get_percentual_conclusao(self, obj):
        meta = 150
        total = obj.aluno.total_horas_integralizadas
        return round((total / meta) * 100, 2)


class ValidacaoSerializer(serializers.ModelSerializer):
    atividade = AtividadeComplementarSerializer(read_only=True)
    atividade_id = serializers.PrimaryKeyRelatedField(
        queryset=AtividadeComplementar.objects.all(),
        source="atividade",
        write_only=True
    )

    coordenador = CoordenadorSerializer(read_only=True)
    coordenador_id = serializers.PrimaryKeyRelatedField(
        queryset=Coordenador.objects.all(),
        source="coordenador",
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Validacao
        fields = "__all__"
        read_only_fields = ["data_analise"]
