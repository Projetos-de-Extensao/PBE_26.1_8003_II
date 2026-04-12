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

UC01 – Efetuar Autenticação
Ator: Aluno / Administrador
Fluxo: Usuário informa suas credenciais → Sistema verifica os dados → Acesso ao sistema é liberado
UC02 – Registrar Atividade Externa
Ator: Aluno
Fluxo: Aluno entra na seção de atividades → Preenche as informações necessárias (categoria, horas, detalhes) → Faz upload do comprovante → Submete para análise
UC03 – Aprovar ou Reprovar Atividade
Ator: Administrador
Fluxo: Admin visualiza atividades em análise → Verifica a documentação enviada → Aprova ou recusa a solicitação → Sistema registra o resultado e atualiza o saldo de horas
UC04 – Acompanhar Carga Horária
Ator: Aluno
Fluxo: Aluno acessa o painel → Sistema apresenta: saldo total de horas, percentual concluído e histórico de atividades registradas
UC05 – Lançar Atividade Interna
Ator: Administrador
Fluxo: Admin cadastra a atividade → Determina a carga horária → Vincula os alunos participantes → Sistema registra as horas automaticamente para cada aluno
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