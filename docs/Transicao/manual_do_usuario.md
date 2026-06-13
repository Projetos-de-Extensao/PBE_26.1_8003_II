# Manual do Usuário — AAC_Refeito

## Visão geral
Este manual descreve como usar o sistema AAC_Refeito (backend Django com páginas minimais). Destina-se a Alunos, Coordenadores e Organizações Acadêmicas.

## Acessando o sistema
1. Abra o navegador e acesse: `http://127.0.0.1:8000/`.
2. Faça login com suas credenciais (usuário e senha).

## Perfis e dashboards
- Aluno: acessa o `Dashboard do Aluno` onde vê total de horas, percentual da meta, atividades internas disponíveis e suas atividades externas.
- Coordenador: acessa o `Dashboard do Coordenador` com lista de atividades pendentes para análise.
- Organização Acadêmica: acessa o `Dashboard da Organização` com atividades internas cadastradas.

## Fluxos comuns (passo a passo)

### 1) Cadastrar atividade externa (Aluno)
1. Entre com sua conta (perfil ALUNO).
2. No dashboard do aluno clique em "Cadastrar Atividade Externa".
3. Preencha:
   - Descrição
   - Carga horária solicitada (número inteiro)
   - Tipo de atividade (selecionar)
4. Clique em "Cadastrar". A atividade ficará com status `PENDENTE`.

### 2) Participar de atividade interna (Aluno)
1. No painel do aluno, em "Atividades Internas Disponíveis", clique em "Participar" na atividade desejada.
2. Sua participação será registrada automaticamente.

### 3) Aprovar atividade externa (Coordenador)
1. Faça login com seu perfil COORDENADOR.
2. No dashboard do coordenador localize a atividade pendente.
3. Clique em "Aprovar".
4. No formulário, preencha a carga horária validada (pode ser igual ou menor que a solicitada, respeitando limites do tipo de atividade) e opcionalmente uma justificativa.
5. Envie; o status mudará para `APROVADO` e as horas serão contabilizadas para o aluno.

### 4) Reprovar atividade externa (Coordenador)
1. No dashboard do coordenador, clique em "Reprovar" na atividade.
2. Informe a justificativa obrigatória.
3. Envie; o status mudará para `REPROVADO` e o aluno receberá o feedback.

### 5) Cadastrar atividade interna (Coordenador / Organização)
1. Acesse "Cadastrar Atividade Interna".
2. Preencha título, descrição, carga horária e tipo de atividade.
3. Salve; a atividade interna ficará disponível para que alunos participem.

## Observações sobre limites e cálculo de horas
- Cada `TipoAtividade` possui `limite_horas_por_evento` e `limite_horas_total`. Ao aprovar, o sistema ajusta a carga validada para não ultrapassar esses limites.
- O total de horas do aluno é recalculado após cada validação (modelo `Aluno.atualizar_total_horas()`).

## Upload de comprovantes
- Atualmente, o backend aceita referência a `caminho_comprovante` (campo `FileField`). Em ambiente de desenvolvimento, coloque os arquivos em `comprovantes/` ou use o formulário na interface web quando disponível.

## APIs úteis
- Documentação de API (se ativada):
  - `/api/schema/` (schema OpenAPI)
  - `/api/docs/` (Swagger)
  - Endpoints principais: `/api/usuarios/`, `/api/alunos/`, `/api/atividades/`, `/api/atividades-internas/`, `/api/validacoes/`

## Executando localmente (recapitulando)
```bash
cd src/backend/AAC_Refeito
.venv/bin/activate   # ou .venv\Scripts\activate no Windows
python manage.py runserver
```