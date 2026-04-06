# 📄 Caso de Uso - Cadastro de Atividade Complementar

## 🎯 Nome
Cadastrar Atividade Complementar

## 👤 Ator Principal
Aluno

## 👥 Atores Secundários
Professor / Coordenação

---

## 📌 Pré-condições
- O aluno deve estar logado no sistema

---

## 🔄 Fluxo Principal

1. Aluno acessa o sistema
2. Aluno seleciona a opção "Cadastrar Atividade"
3. Aluno preenche os dados da atividade (nome, carga horária, tipo)
4. Aluno anexa o comprovante
5. Sistema valida os dados
6. Sistema registra a atividade
7. Sistema define o status como "Pendente"
8. Sistema exibe confirmação ao aluno

---

## 🔁 Fluxos Alternativos

### Dados inválidos
- Sistema solicita correção dos dados

### Falha no upload
- Sistema exibe erro e solicita novo envio

---

## ✅ Pós-condições
- Atividade cadastrada no sistema
- Atividade aguardando validação