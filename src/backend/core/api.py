from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

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
from .permissions import IsCoordenadorOrReadOnly, IsDonoAlunoOuCoordenador
from .serializers import (
    UsuarioSerializer,
    AlunoSerializer,
    CoordenadorSerializer,
    OrgAcademicaSerializer,
    EixoTematicoSerializer,
    TipoAtividadeSerializer,
    AtividadeComplementarSerializer,
    ValidacaoSerializer,
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.select_related("usuario").all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]


class CoordenadorViewSet(viewsets.ModelViewSet):
    queryset = Coordenador.objects.select_related("usuario").all()
    serializer_class = CoordenadorSerializer
    permission_classes = [IsAdminUser]


class OrgAcademicaViewSet(viewsets.ModelViewSet):
    queryset = OrgAcademica.objects.select_related("usuario").all()
    serializer_class = OrgAcademicaSerializer
    permission_classes = [IsAuthenticated]


class EixoTematicoViewSet(viewsets.ModelViewSet):
    queryset = EixoTematico.objects.all()
    serializer_class = EixoTematicoSerializer
    permission_classes = [IsCoordenadorOrReadOnly]


class TipoAtividadeViewSet(viewsets.ModelViewSet):
    queryset = TipoAtividade.objects.select_related("eixo_tematico").all()
    serializer_class = TipoAtividadeSerializer
    permission_classes = [IsCoordenadorOrReadOnly]


class AtividadeComplementarViewSet(viewsets.ModelViewSet):
    queryset = AtividadeComplementar.objects.select_related(
        "aluno__usuario",
        "coordenador__usuario",
        "organizacao__usuario",
        "tipo_atividade__eixo_tematico",
    ).all()
    serializer_class = AtividadeComplementarSerializer
    permission_classes = [IsAuthenticated, IsDonoAlunoOuCoordenador]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_staff or getattr(usuario, "perfil", None) == Usuario.Perfil.COORDENADOR:
            return self.queryset

        if getattr(usuario, "perfil", None) == Usuario.Perfil.ALUNO:
            return self.queryset.filter(aluno__usuario=usuario)

        if getattr(usuario, "perfil", None) == Usuario.Perfil.ORG:
            return self.queryset.filter(organizacao__usuario=usuario)

        return self.queryset.none()

    @action(detail=True, methods=["post"], permission_classes=[IsCoordenadorOrReadOnly])
    def aprovar(self, request, pk=None):
        atividade = self.get_object()
        coordenador = Coordenador.objects.filter(usuario=request.user).first()

        if not coordenador:
            return Response(
                {"erro": "Apenas coordenadores podem aprovar atividades."},
                status=status.HTTP_403_FORBIDDEN
            )

        carga = request.data.get("carga_horaria_validada")
        justificativa = request.data.get("justificativa", "")

        atividade.aprovar(
            coordenador=coordenador,
            carga_horaria_validada=int(carga) if carga else None,
            justificativa=justificativa
        )

        serializer = self.get_serializer(atividade)
        return Response(serializer.data)

    @action(detail=True, methods=["post"], permission_classes=[IsCoordenadorOrReadOnly])
    def reprovar(self, request, pk=None):
        atividade = self.get_object()
        coordenador = Coordenador.objects.filter(usuario=request.user).first()
        justificativa = request.data.get("justificativa")

        if not coordenador:
            return Response(
                {"erro": "Apenas coordenadores podem reprovar atividades."},
                status=status.HTTP_403_FORBIDDEN
            )

        if not justificativa:
            return Response(
                {"erro": "Informe uma justificativa para reprovar."},
                status=status.HTTP_400_BAD_REQUEST
            )

        atividade.reprovar(coordenador=coordenador, justificativa=justificativa)

        serializer = self.get_serializer(atividade)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def resumo(self, request):
        usuario = request.user

        if getattr(usuario, "perfil", None) != Usuario.Perfil.ALUNO:
            return Response(
                {"erro": "Resumo disponível apenas para alunos."},
                status=status.HTTP_403_FORBIDDEN
            )

        aluno = Aluno.objects.get(usuario=usuario)
        total = aluno.atualizar_total_horas()
        meta = 150

        return Response({
            "aluno": aluno.usuario.username,
            "matricula": aluno.matricula,
            "total_horas_integralizadas": total,
            "meta_horas": meta,
            "percentual_conclusao": round((total / meta) * 100, 2),
            "atividades_pendentes": aluno.atividades.filter(status=AtividadeComplementar.Status.PENDENTE).count(),
            "atividades_aprovadas": aluno.atividades.filter(status=AtividadeComplementar.Status.APROVADO).count(),
            "atividades_reprovadas": aluno.atividades.filter(status=AtividadeComplementar.Status.REPROVADO).count(),
        })


class ValidacaoViewSet(viewsets.ModelViewSet):
    queryset = Validacao.objects.select_related(
        "atividade",
        "coordenador__usuario"
    ).all()
    serializer_class = ValidacaoSerializer
    permission_classes = [IsCoordenadorOrReadOnly]
