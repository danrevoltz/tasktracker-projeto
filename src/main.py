"""
TaskTracker - Fase 2 (Bootcamp II)
Aplicação CLI de Gerenciamento de Tarefas em Python 3.
"""

def ler_titulo():
    """Lê e valida o título da tarefa (rejeita vazios ou apenas espaços)."""
    while True:
        titulo = input("Digite o título da tarefa: ").strip()
        if titulo:
            return titulo
        print("❌ ERRO: O título não pode ser vazio. Digite um título válido.\n")

def ler_descricao():
    """Lê a descrição da tarefa (detalhamento livre)."""
    return input("Digite a descrição da tarefa (opcional): ").strip()

def ler_prioridade():
    """Lê e valida estritamente a prioridade ('Alta', 'Média' ou 'Baixa')."""
    prioridades_validas = ["alta", "média", "media", "baixa"]
    while True:
        prioridade = input("Digite a prioridade (Alta, Média ou Baixa): ").strip().capitalize()
        if prioridade == "Media":
            prioridade = "Média"
        
        if prioridade.lower() in prioridades_validas:
            return prioridade
        print("❌ ERRO: Prioridade inválida! Aceita exclusivamente 'Alta', 'Média' ou 'Baixa'.\n")

def ler_data_limite():
    """Lê a data limite planejada (formato livre ou DD/MM/AAAA)."""
    data = input("Digite a data limite (ex: DD/MM/AAAA ou 'A combinar'): ").strip()
    return data if data else "Não informada"

def cadastrar_tarefa(tarefas):
    """Cadastra uma nova tarefa na estrutura de dados."""
    print("\n" + "="*45)
    print("         CADASTRO DE NOVA TAREFA")
    print("="*45)
    
    titulo = ler_titulo()
    descricao = ler_descricao()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()
    status = "Pendente"
    
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": status
    }
    
    tarefas.append(nova_tarefa)
    print("\n✅ Tarefa cadastrada com sucesso!")

def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas organizadamente."""
    print("\n" + "="*45)
    print("       LISTA DE TAREFAS CADASTRADAS")
    print("="*45)
    
    if not tarefas:
        print("\nℹ️ Nenhuma tarefa cadastrada no momento.")
        return

    for idx, tarefa in enumerate(tarefas, 1):
        print(f"\n--- Tarefa #{idx} ---")
        print(f"📌 Título:      {tarefa['titulo']}")
        print(f"📝 Descrição:   {tarefa['descricao'] if tarefa['descricao'] else 'Sem descrição'}")
        print(f"⚡ Prioridade:  {tarefa['prioridade']}")
        print(f"📅 Data Limite: {tarefa['data_limite']}")
        print(f"🔄 Status:      {tarefa['status']}")
    print("-" * 45)

def menu_principal():
    """Exibe o menu contínuo e gerencia a navegação do usuário."""
    tarefas = []
    
    while True:
        print("\n" + "="*45)
        print("        TASKTRACKER - MENU PRINCIPAL")
        print("="*45)
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        print("="*45)
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\n👋 Encerrando a aplicação TaskTracker. Até mais!")
            break
        else:
            print("\n❌ Opção inválida! Selecione 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()
```[cite: 2, 3]

---

### Resumo da estrutura final no seu computador:[cite: 2]

```plaintext
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```[cite: 2]