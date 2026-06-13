---
id: dt
title: Design Thinking - AAC_Refeito
---

## 1. Capa

- Título do Projeto: AAC_Refeito
- Equipe: Bento Couto, Maria Luisa Martinelli, Miguel
- Data: 13/06/2026
- Organização: Projeto Acadêmico IBMEC

---

## 2. Introdução

- **Contexto do Projeto**: O AAC_Refeito busca digitalizar a gestão de Atividades Acadêmicas Complementares por meio de um backend Django com APIs REST e dashboards web simples.
- **Objetivo**: Reduzir a burocracia no registro, validação e acompanhamento de atividades complementares dos alunos.
- **Público-Alvo**: Alunos, coordenadores e organizações acadêmicas que participam do processo de validação das AACs.
- **Escopo**: Backend Django com autenticação de perfis, cadastro de atividades externas e internas, aprovação/reprovação e cálculo de horas validada.

---

## 3. Fases do Design Thinking

### 3.1. Empatia

- **Pesquisa**: A equipe analisou requisitos de uso de alunos, coordenadores e organizações, identificando itens como registro de atividades, acompanhamento de horas e aprovação de solicitações.
- **Insights**: Usuários precisam de transparência no status das atividades e de um caminho claro para aprovar ou reprovar solicitações.
- **Personas**:
  - Aluno que precisa registrar atividades e acompanhar horas.
  - Coordenador que valida atividades externas.
  - Organização acadêmica que cadastra atividades internas.

### 3.2. Definição

- **Problema Central**: Como criar um sistema confiável e centralizado para o controle de Atividades Acadêmicas Complementares?
- **Pontos de Vista (POV)**:
  - "O aluno precisa ver suas horas aprovadas sem depender de planilhas."  
  - "O coordenador precisa aprovar atividades com um fluxo simples."  
  - "A organização precisa cadastrar e gerenciar atividades internas com clareza."

### 3.3. Ideação

- **Brainstorming**: Foram levantadas ideias de perfis separados, tipos de atividades, status de aprovação e listas de atividades.
- **Seleção de Ideias**: Priorizou-se a implementação do backend em Django e o uso de APIs REST para permitir a integração futura com um frontend mais completo.
- **Ideias Selecionadas**:
  - Dashboard diferenciado para cada perfil.
  - Modelo de validação para aprovar/reprovar atividades.
  - Relações entre aluno, atividade, tipo de atividade e eixo temático.

### 3.4. Prototipagem

- **Descrição do Protótipo**: O protótipo foi construído em código com páginas Django e formulários básicos, sem foco em interface visual avançada.
- **Materiais Utilizados**: Python, Django, Django REST Framework, HTML/CSS e MkDocs para documentação.
- **Testes Realizados**: Testes manuais de login, cadastro de atividades, participação em atividades internas e aprovação de atividades externas.

### 3.5. Teste

- **Feedback dos Usuários**: A equipe testou internamente os fluxos de aluno, coordenador e organização e ajustou permissões e status.
- **Ajustes Realizados**: Inclusão do `TipoAtividade`, do cálculo de `total_horas_integralizadas` e do modelo `Validacao` para registrar decisões de aprovação.
- **Resultados Finais**: Um backend funcional com rotas API e dashboards que suportam os casos de uso essenciais.

---

## 4. Conclusão

- **Resultados Obtidos**: Sistema backend operacional para gerenciamento de AACs, com três perfis de usuário e rotas de API.
- **Próximos Passos**: Melhorar a interface visual, implementar upload de comprovantes nos formulários e adicionar testes automatizados.
- **Aprendizados**: A equipe aprendeu a modelar usuários e relacionamentos no Django, criar APIs REST e documentar o projeto para deploy.

---

## 5. Anexos

- Ver `docs/Elaboracao/diagrama_de_classes.md` e `docs/Elaboracao/casos_de_uso.md` para diagramas e fluxos de uso do AAC_Refeito.

---

## Dicas

- Use linguagem clara e objetiva.
- Descreva os fluxos atuais do backend.
- Relacione cada fase do Design Thinking com as funcionalidades implementadas.

