from rest_framework import permissions

from .models import Usuario


class IsCoordenadorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_staff
                or getattr(request.user, "perfil", None) == Usuario.Perfil.COORDENADOR
            )
        )


class IsDonoAlunoOuCoordenador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff or getattr(request.user, "perfil", None) == Usuario.Perfil.COORDENADOR:
            return True

        aluno = getattr(obj, "aluno", None)
        return aluno and aluno.usuario_id == request.user.id
