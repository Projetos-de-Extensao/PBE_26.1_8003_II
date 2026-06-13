#  Casos de Uso - Projeto AAC_Refeito

## Caso de Uso 1: Cadastro de Atividade Externa

### Ator Principal
Aluno

### Atores Secundários
Coordenador

### Pré-condições
- Usuário autenticado com perfil ALUNO.
- O aluno possui perfil `Aluno` cadastrado no sistema.

### Fluxo Básico
1. O aluno faz login no sistema.
2. O aluno acessa a página de cadastro de atividade externa.
3. O aluno preenche descrição, carga horária e escolhe o tipo de atividade.
4. O aluno envia o formulário.
5. O sistema cria a `AtividadeComplementar` com status `PENDENTE`.
6. A atividade fica disponível para análise do coordenador.

### Fluxos Alternativos
- Dados inválidos: o sistema exibe erro e solicita correção.
- Usuário não autenticado: redireciona para login.

### Pós-condições
- A atividade externa foi registrada.
- O status da atividade é `PENDENTE`.

---

## Caso de Uso 2: Aprovação de Atividade Externa

### Ator Principal
Coordenador

### Atores Secundários
Aluno

### Pré-condições
- Usuário autenticado com perfil COORDENADOR.
- Existem atividades externas com status `PENDENTE`.

### Fluxo Básico
1. O coordenador faz login no sistema.
2. O coordenador acessa o dashboard de atividades pendentes.
3. O coordenador seleciona uma atividade para análise.
4. O coordenador informa a carga horária validada e justificativa.
5. O sistema define o status como `APROVADO` e registra a validação.
6. O total de horas do aluno é atualizado.

### Fluxos Alternativos
- Carga horária inválida: o sistema exibe erro.
- Atividade reprovada: o coordenador escolhe reprovar e registra justificativa.

### Pós-condições
- A atividade externa recebe status `APROVADO` ou `REPROVADO`.
- O registro de validação é criado ou atualizado.

---

## Caso de Uso 3: Cadastro de Atividade Interna

### Ator Principal
Coordenador / Organização Acadêmica

### Atores Secundários
Aluno

### Pré-condições
- Usuário autenticado com perfil COORDENADOR ou ORG.

### Fluxo Básico
1. O coordenador ou organização acessa o formulário de cadastro de atividade interna.
2. O usuário informa título, descrição, carga horária e tipo de atividade.
3. O sistema salva a `AtividadeInterna`.

### Fluxos Alternativos
- Campos faltando ou inválidos: o sistema exibe mensagem de erro.

### Pós-condições
- A atividade interna foi cadastrada no sistema.
- A atividade fica disponível para participação pelos alunos.

---

## Caso de Uso 4: Participar de Atividade Interna

### Ator Principal
Aluno

### Atores Secundários
Nenhum

### Pré-condições
- Usuário autenticado com perfil ALUNO.
- Existência de atividades internas cadastradas.

### Fluxo Básico
1. O aluno acessa a lista de atividades internas.
2. O aluno escolhe uma atividade e solicita participação.
3. O sistema registra a participação do aluno na atividade.

### Pós-condições
- O aluno é adicionado à lista de participantes da `AtividadeInterna`.

