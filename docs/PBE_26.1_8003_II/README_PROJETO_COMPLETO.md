# Projeto AAC Completo

Sistema de Atividades Acadêmicas Complementares desenvolvido em Django REST Framework.

## Estrutura

### backend/
Código completo da API REST:
- models
- serializers
- views
- permissões
- admin
- autenticação
- upload de comprovantes
- cálculo de horas
- validação de atividades

### documentacao/
Documentação acadêmica:
- requisitos
- casos de uso
- arquitetura
- RUP
- brainstorm
- diagramas
- protótipos

### assets/
Imagens, logos e diagramas do projeto.

## Como executar

Instale as dependências:

pip install django djangorestframework

Execute:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## URLs

Admin:
http://127.0.0.1:8000/admin/

API:
http://127.0.0.1:8000/api/
