---
id: mapa_mental_atividades
title: Mapa Mental - Projeto AAC_Refeito
---

## Introdução

<p align="justify">
O mapa mental descreve as funcionalidades e os perfis do sistema AAC_Refeito, um backend Django para gestão de Atividades Acadêmicas Complementares.
</p>

## Mapa Mental - Projeto AAC_Refeito

```mermaid
mindmap
  root((AAC_Refeito))
    Aluno
      Cadastro de atividade externa
      Participar atividade interna
      Visualizar horas validadas
      Consultar status de atividades
    Coordenador
      Aprovar atividades externas
      Reprovar atividades externas
      Cadastrar atividade interna
      Ver atividades pendentes
    Organização
      Cadastrar atividades internas
      Gerenciar participantes
      Consultar atividades lançadas
    Atividade
      Externa
        Descrição
        Carga horária solicitada
        Tipo de atividade
        Status
      Interna
        Título
        Descrição
        Carga horária
        Participantes
    Modelos
      Usuario
      Aluno
      Coordenador
      OrgAcademica
      TipoAtividade
      AtividadeComplementar
      AtividadeInterna
      Validacao
    API
      /api/usuarios/
      /api/alunos/
      /api/atividades/
      /api/atividades-internas/
      /api/validacoes/
```

## Conclusão

<p align="justify">
O sistema AAC_Refeito organiza as atividades complementares em três perfis e disponibiliza os principais fluxos necessários para cadastro, validação e acompanhamento de horas de forma integrada.
</p>

## Referências

> Faculdade IBMEC. Documentação de Atividades Acadêmicas Complementares. 2026.

## Versionamento

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 13/06/2026 | 1.1 | Atualização para o projeto AAC_Refeito | Miguel, Maria Luisa e Bento |