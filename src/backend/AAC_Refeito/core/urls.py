from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("aluno/", views.dashboard_aluno, name="dashboard_aluno"),
    path("coordenador/", views.dashboard_coordenador, name="dashboard_coordenador"),
    path("organizacao/", views.dashboard_organizacao, name="dashboard_organizacao"),
    path(
        "atividade-interna/cadastrar/",
        views.cadastrar_atividade_interna,
        name="cadastrar_atividade_interna"
    ),
    path(
        "atividades-internas/<int:atividade_id>/participar/",
        views.participar_atividade_interna,
        name="participar_atividade_interna"
    ),
    path(
        "atividade-externa/cadastrar/",
        views.cadastrar_atividade_externa,
        name="cadastrar_atividade_externa"
    ),
    path(
        "atividade/<int:atividade_id>/aprovar/",
        views.aprovar_atividade,
        name="aprovar_atividade"
    ),
    path(
        "atividade/<int:atividade_id>/reprovar/",
        views.reprovar_atividade,
        name="reprovar_atividade"
    ),
]