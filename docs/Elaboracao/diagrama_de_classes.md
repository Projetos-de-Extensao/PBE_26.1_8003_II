#  Diagrama de Classes - Projeto AAC_Refeito

## Visão Geral

O sistema AAC_Refeito foi modelado com os seguintes principais objetos:

- `Usuario` (customizado, herdado de `AbstractUser`)
- `Aluno`
- `Coordenador`
- `OrgAcademica`
- `EixoTematico`
- `TipoAtividade`
- `AtividadeComplementar`
- `AtividadeInterna`
- `Validacao`

## Diagrama de Classes Simplificado

```mermaid
classDiagram
    class Usuario {
        +String username
        +String email
        +String perfil
    }
    class Aluno {
        +String matricula
        +String curso
        +int semestre_ingresso
        +int total_horas_integralizadas
        +atualizar_total_horas()
    }
    class Coordenador {
        +String sia_funcionario
    }
    class OrgAcademica {
        +String nome_entidade
        +String cargo_representante
    }
    class EixoTematico {
        +String nome
        +String descricao
    }
    class TipoAtividade {
        +String nome
        +int limite_horas_total
        +int limite_horas_por_evento
    }
    class AtividadeComplementar {
        +String descricao
        +Date data_realizacao
        +int carga_horaria_solicitada
        +int carga_horaria_validada
        +String status
        +String tipo_origem
        +String caminho_comprovante
        +String feedback
        +DateTime criado_em
        +DateTime atualizado_em
        +aprovar()
        +reprovar()
    }
    class AtividadeInterna {
        +String titulo
        +String descricao
        +int carga_horaria
        +DateTime criado_em
    }
    class Validacao {
        +String resultado
        +int carga_horaria_validada
        +String justificativa
        +DateTime data_analise
    }

    Usuario <|-- Aluno
    Usuario <|-- Coordenador
    Usuario <|-- OrgAcademica
    Aluno "1" -- "*" AtividadeComplementar : aluno
    Coordenador "1" -- "*" AtividadeComplementar : coordenador
    OrgAcademica "1" -- "*" AtividadeComplementar : organizacao
    TipoAtividade "1" -- "*" AtividadeComplementar : tipo_atividade
    TipoAtividade "1" -- "*" AtividadeInterna : tipo_atividade
    OrgAcademica "1" -- "*" AtividadeInterna : organizacao
    Coordenador "1" -- "*" AtividadeInterna : coordenador
    Aluno "*" -- "*" AtividadeInterna : participantes
    AtividadeComplementar "1" -- "1" Validacao : validacao
```

## Descrição das Classes

- `Usuario`: usuário personalizado com o campo `perfil` (ALUNO, COORDENADOR, ORG).
- `Aluno`: armazena matrícula, curso, semestre e total de horas integralizadas.
- `Coordenador`: representa o usuário que analisa atividades externas.
- `OrgAcademica`: representa a organização responsável por cadastrar atividades internas.
- `EixoTematico`: define uma categoria geral para tipos de atividade.
- `TipoAtividade`: define limites de horas e pertence a um eixo temático.
- `AtividadeComplementar`: representa atividades externas solicitadas por alunos e validadas por coordenadores.
- `AtividadeInterna`: representa atividades lançadas por coordenadores ou organizações e com participantes.
- `Validacao`: registra resultado, carga validada e justificativa das análises de atividades complementares.

## Observações

- O método `Aluno.atualizar_total_horas()` calcula o total de horas aprovadas com base nas atividades complementares com status `APROVADO`.
- O método `AtividadeComplementar.aprovar()` ajusta a carga validada conforme o limite do tipo de atividade e atualiza o histórico de validação.
- `AtividadeInterna` tem uma relação de muitos-para-muitos com `Aluno` para registrar participantes.

