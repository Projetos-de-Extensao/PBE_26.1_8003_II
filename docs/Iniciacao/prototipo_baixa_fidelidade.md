---
id: prototipobaixa
title: Protótipo - Projeto AAC_Refeito
---
## Introdução

<p align = "justify">
O protótipo de baixa fidelidade descreve a interface e os fluxos atuais do projeto AAC_Refeito, que está implementado como um backend Django com templates HTML para login, dashboards e formulários de atividades.
</p>

## Metodologia

<p align = "justify">
A equipe desenvolveu o protótipo diretamente no código, usando páginas Django simples para representar os fluxos de aluno, coordenador e organização. O foco foi validar as funcionalidades do backend antes de avançar para uma interface visual maior.
</p>

## Protótipo de baixa fidelidade

### Versão 1.0

### Tela Login

- Página de login básica com campos de usuário e senha.
- Autenticação redireciona para o dashboard adequado conforme o perfil.

### Tela Dashboard do Aluno

- Exibe total de horas integralizadas.
- Mostra percentual de conclusão da meta.
- Lista atividades externas do aluno e atividades internas disponíveis para participação.

### Tela Dashboard do Coordenador

- Lista atividades externas pendentes.
- Permite aprovar ou reprovar atividades.
- Acesso ao formulário de cadastro de atividades internas.

### Tela Dashboard da Organização

- Mostra atividades internas cadastradas pela organização.
- Permite consultar participantes de cada atividade.

### Tela Cadastrar Atividade Externa

- Formulário para descrição, carga horária solicitada e tipo de atividade.
- Ao enviar, a atividade fica com status PENDENTE.

### Tela Cadastrar Atividade Interna

- Formulário para título, descrição, carga horária e tipo de atividade.
- Pode ser acessada por coordenador ou organização.

### Tela Aprovar Atividade

- Formulário de aprovar atividade com campo de carga horária validada e justificativa.
- Atualiza o status e o total de horas do aluno.

### Tela Reprovar Atividade

- Formulário para registrar justificativa de reprovação.
- Atualiza o status da atividade para REPROVADO.

## Conclusão

<p align = "justify">
A primeira versão do protótipo priorizou a funcionalidade do backend e os fluxos de uso mais importantes para o AAC_Refeito. O design atual é simples e permite documentar o projeto para deploy e evolução futura.
</p>

## Referências

> Django. Disponível em: https://www.djangoproject.com/  
> Django REST Framework. Disponível em: https://www.django-rest-framework.org/  

## Autor(es)

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 13/06/2026 | 1.0 | Atualização para o projeto AAC_Refeito | Miguel, Maria Luisa e Bento |
| 07/09/20 | 1.0     | Criação do documento                 | Lucas Alexandre e Matheus Estanislau                                                 |
| 07/09/20 | 1.1     | Adicionado as imagens do protótipo    | Lucas Alexandre e Matheus Estanislau                                                 |
| 07/09/20 | 1.2     | Adicionado conclusão e referências   | Lucas Alexandre e Matheus Estanislau                                                 |
| 26/10/20 | 2.0     | Adicionada a versão 2.0 do protótipo | João Pedro, Lucas Alexandre, Matheus Estanislau, Moacir Mascarenha e Renan Cristyan |
