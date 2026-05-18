# Implementação Back-End AAC

Sistema de Atividades Acadêmicas Complementares em Django REST Framework.

## Arquivos principais

- `core/models.py`: entidades do sistema.
- `core/serializers.py`: conversão dos models para JSON.
- `core/api.py`: ViewSets e ações de aprovar/reprovar.
- `core/api_urls.py`: rotas da API.
- `core/admin.py`: cadastro dos models no painel admin.
- `aac/urls.py`: rotas principais do projeto.
- `aac/settings_trecho_para_adicionar.py`: trecho para copiar no `settings.py`.

## Endpoints

- `/api/usuarios/`
- `/api/alunos/`
- `/api/coordenadores/`
- `/api/organizacoes/`
- `/api/eixos/`
- `/api/tipos-atividade/`
- `/api/atividades/`
- `/api/atividades/resumo/`
- `/api/atividades/{id}/aprovar/`
- `/api/atividades/{id}/reprovar/`
- `/api/validacoes/`

## Comandos

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Observação importante

Como o model `Usuario` herda de `AbstractUser`, o `AUTH_USER_MODEL = "core.Usuario"` deve estar no `settings.py` antes da primeira migração do banco.
Se seu banco já tiver migrations antigas, o mais simples no projeto escolar é apagar `db.sqlite3` e recriar as migrations.
