#  Caso de Uso - Cadastro de Atividade Externa

##  Nome
Cadastrar Atividade Externa

##  Ator Principal
Aluno

##  Atores Secundários
Coordenador

---

##  Pré-condições
- O aluno deve estar autenticado no sistema.
- O aluno deve ter perfil de usuário do tipo ALUNO.

---

##  Fluxo Principal

1. O aluno acessa a página de login e informa usuário e senha.
2. O sistema valida as credenciais e redireciona o aluno para o dashboard.
3. O aluno seleciona a opção de cadastrar atividade externa.
4. O aluno preenche a descrição, a carga horária solicitada e o tipo de atividade.
5. O sistema cria uma Atividade Complementar com status PENDENTE.
6. O coordenador visualiza a atividade pendente no dashboard do coordenador.
7. O coordenador aprova ou reprova a atividade externa.
8. O sistema atualiza o status da atividade e, em caso de aprovação, calcula a carga horária validada.

---

## Fluxos Alternativos

### Dados inválidos
- Se o aluno enviar descrição ou carga horária inválida, o sistema exibe mensagem de erro e solicita correção.

### Usuário não autenticado
- Se um usuário sem sessão tentar acessar a página de cadastro, ele é redirecionado para a página de login.

### Atividade reprovada
- Se o coordenador reprovar a atividade, o sistema define o status como REPROVADO, registra a justificativa e não adiciona horas ao aluno.

---

## Pós-condições
- A atividade externa fica registrada no sistema com status PENDENTE.
- O coordenador pode aprovar ou reprovar a solicitação.
- O total de horas validado do aluno será atualizado somente após aprovação.
