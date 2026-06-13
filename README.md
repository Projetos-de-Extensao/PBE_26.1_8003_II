# Projeto Back-End (AAC_Refeito)

**Código da Disciplina**: IBM8936

## Sobre
Projeto desenvolvido para a disciplina/projeto de extensão PBE 26.1 8003 II. O repositório contém um backend em Django/Django REST Framework para gerenciar Atividades Acadêmicas Complementares (AAC).

O backend principal está em `src/backend/AAC_Refeito` e fornece APIs e páginas Django mínimas para os perfis: Aluno, Coordenador e Organização Acadêmica.

## Requisitos
- Python 3.10+ (ou compatível com as dependências listadas)
- Git
- (Opcional) virtualenv / venv

## Instalação (Windows)

Abra o PowerShell ou CMD e execute:

```powershell
cd src\backend\AAC_Refeito
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Caso seja a primeira vez, crie as migrações e aplique-as
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

Depois abra `http://127.0.0.1:8000/` para acessar a página de login e `http://127.0.0.1:8000/admin/` para o painel administrativo.

## Instalação (Linux / macOS)

```bash
cd src/backend/AAC_Refeito
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

