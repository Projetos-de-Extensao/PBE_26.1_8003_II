# 📄 Fluxo do Sistema - Cadastro de Atividade

```text
Início
 ↓
Login do aluno
 ↓
Selecionar "Cadastrar Atividade"
 ↓
Preencher dados
 ↓
Anexar comprovante
 ↓
Dados válidos?
 ├── NÃO → Solicita correção
 └── SIM
      ↓
Salvar atividade
 ↓
Definir status como "Pendente"
 ↓
Fim


---

# 📁 **4. diagrama-caso-uso.md**
```md id="p4v8zc"
# 📄 Diagrama de Caso de Uso (UML)

```text
          +----------------------------------+
          | Sistema de Atividades Acadêmicas |
          +----------------------------------+

   (Aluno) ------------> (Login)

   (Aluno) ------------> (Cadastrar Atividade)
                                 |
                                 v
                        (Anexar Comprovante)
                                 |
                                 v
                        (Enviar para Validação)

   (Aluno) ------------> (Visualizar Atividades)

   (Professor) --------> (Validar Atividade)
                                 |
                                 v
                        (Atualizar Status)