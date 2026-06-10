from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import (
    UsuarioViewSet,
    AlunoViewSet,
    CoordenadorViewSet,
    OrgAcademicaViewSet,
    EixoTematicoViewSet,
    TipoAtividadeViewSet,
    AtividadeComplementarViewSet,
    AtividadeInternaViewSet,
    ValidacaoViewSet,
)

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuario")
router.register(r"alunos", AlunoViewSet, basename="aluno")
router.register(r"coordenadores", CoordenadorViewSet, basename="coordenador")
router.register(r"organizacoes", OrgAcademicaViewSet, basename="organizacao")
router.register(r"eixos", EixoTematicoViewSet, basename="eixo")
router.register(r"tipos-atividade", TipoAtividadeViewSet, basename="tipo-atividade")
router.register(r"atividades", AtividadeComplementarViewSet, basename="atividade")
router.register(r"atividades-internas", AtividadeInternaViewSet, basename="atividade-interna")
router.register(r"validacoes", ValidacaoViewSet, basename="validacao")

urlpatterns = [
    path("", include(router.urls)),
]
