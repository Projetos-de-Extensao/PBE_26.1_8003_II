from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Perfil do sistema", {"fields": ("perfil",)}),
    )
    list_display = ("username", "email", "perfil", "is_staff", "is_active")
    list_filter = ("perfil", "is_staff", "is_active")


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "matricula", "curso", "semestre_ingresso", "total_horas_integralizadas")
    search_fields = ("usuario__username", "matricula", "curso")


@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):
    list_display = ("usuario", "sia_funcionario")
    search_fields = ("usuario__username", "sia_funcionario")


@admin.register(OrgAcademica)
class OrgAcademicaAdmin(admin.ModelAdmin):
    list_display = ("nome_entidade", "cargo_representante", "usuario")
    search_fields = ("nome_entidade", "usuario__username")


@admin.register(EixoTematico)
class EixoTematicoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(TipoAtividade)
class TipoAtividadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "eixo_tematico", "limite_horas_total", "limite_horas_por_evento")
    list_filter = ("eixo_tematico",)
    search_fields = ("nome",)


@admin.register(AtividadeComplementar)
class AtividadeComplementarAdmin(admin.ModelAdmin):
    list_display = ("descricao", "aluno", "tipo_atividade", "status", "carga_horaria_solicitada", "carga_horaria_validada")
    list_filter = ("status", "tipo_origem", "tipo_atividade")
    search_fields = ("descricao", "aluno__usuario__username", "aluno__matricula")


@admin.register(Validacao)
class ValidacaoAdmin(admin.ModelAdmin):
    list_display = ("atividade", "coordenador", "resultado", "carga_horaria_validada", "data_analise")
    list_filter = ("resultado", "data_analise")
