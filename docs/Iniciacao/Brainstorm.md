---
id: brainstorm_atividades
title: Brainstorm - Projeto AAC_Refeito
---

## Introdução
<p align = "justify">
O brainstorm documenta as principais decisões da equipe para o projeto AAC_Refeito, um sistema para gerenciar Atividades Acadêmicas Complementares via backend Django e APIs REST.
</p>

## Metodologia
<p align = "justify">
A equipe analisou o código existente em `src/backend/AAC_Refeito` e gerou ideias para os três perfis de usuário: aluno, coordenador e organização acadêmica. O brainstorm focou em funcionalidades reais e no escopo do backend implementado.
</p>

## Principais ideias levantadas

### Objetivo principal da aplicação

<p align = "justify">
<b>Aluno 1</b> - Permitir que estudantes registrem atividades acadêmicas complementares e consultem o andamento de suas horas.

<b>Aluno 2</b> - Oferecer um painel de progresso com horas integralizadas, meta e atividades pendentes.

<b>Aluno 3</b> - Registrar atividades externas e internas com categorização por tipo de atividade.

<b>Aluno 4</b> - Dar à coordenação um fluxo de aprovação/reprovação de atividades externas.

<b>Aluno 5</b> - Disponibilizar uma organização acadêmica para cadastrar atividades internas e acompanhar participantes.
</p>

---

### Cadastro de usuários e perfis

<p align = "justify">
<b>Aluno 1</b> - Usuários são criados com perfis separados para Aluno, Coordenador e Organização Acadêmica.

<b>Aluno 2</b> - A autenticação usa o login padrão do Django, com redirecionamento para dashboards específicos.

<b>Aluno 3</b> - O perfil contém informações de matrícula, curso e tipo de usuário.
</p>

---

### Cadastro de atividades

<p align = "justify">
<b>Aluno 1</b> - Alunos cadastram atividades externas com descrição, carga horária e tipo de atividade.

<b>Aluno 2</b> - Coordenadores e organizações cadastram atividades internas que podem ser participadas pelos alunos.

<b>Aluno 3</b> - Cada atividade interna tem título, descrição, carga horária e tipo de atividade.
</p>

---

### Validação de atividades

<p align = "justify">
<b>Aluno 1</b> - Coordenadores analisam atividades externas pendentes e podem aprovar ou reprovar.

<b>Aluno 2</b> - O sistema registra a decisão em um objeto de validação e atualiza a carga horária validada do aluno.

<b>Aluno 3</b> - Atividades reprovadas recebem feedback do coordenador e ficam com status de rejeitado.
</p>

---

### Informações importantes para o usuário

<p align = "justify">
<b>Aluno 1</b> - O aluno precisa ver total de horas integralizadas e percentual da meta.

<b>Aluno 2</b> - O coordenador deve ver atividades pendentes e o resultado das análises.

<b>Aluno 3</b> - A organização deve acompanhar as atividades internas que cadastrou e seus participantes.
</p>

---

### Requisitos elicitados atuais

|ID|Descrição|
|---|---|
|BS01|O sistema deve permitir autenticação de usuários por perfil.| 
|BS02|O sistema deve tratar perfis de Aluno, Coordenador e Organização Acadêmica.| 
|BS03|O aluno deve cadastrar atividades externas.| 
|BS04|O sistema deve permitir cadastro de atividades internas por coordenador ou organização.| 
|BS05|O aluno deve participar de atividades internas disponíveis.| 
|BS06|O coordenador deve aprovar ou reprovar atividades externas.| 
|BS07|O sistema deve calcular e atualizar total de horas validadas.| 
|BS08|O aluno deve visualizar seu painel de horas e atividades.| 
|BS09|Deve haver uma API REST para gerenciar usuários, atividades e validações.| 
|BS10|As atividades devem ser categorizadas por tipo de atividade e eixo temático.| 

## Conclusão
<p align = "justify">
O brainstorm consolidou o escopo do projeto AAC_Refeito em torno de três perfis e de funcionalidades que já existem no backend atual. A documentação futura deve focar em APIs, fluxos de aprovação e no cálculo de horas validadas.
</p>

## Referências Bibliográficas

> Django REST Framework. Disponível em: https://www.django-rest-framework.org/  

## Autor(es)

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 13/06/2026 | 1.1 | Atualização para o projeto AAC_Refeito | Miguel, Maria Luisa e Bento |