from contato import Contato

def menu():
    c = Contato()
    while True:
        print("\n=== Menu Contatos ===")
        print("1. Adicionar contato")
        print("2. Atualizar nome")
        print("3. Atualizar email")
        print("4. Atualizar telefone")
        print("5. Apagar contato")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            c.adicionar_contato(nome, email, telefone)
        elif opcao == "2":
            id_ = input("ID do contato: ")
            nome = input("Novo nome: ")
            c.atualizar_nome(id_, nome)
        elif opcao == "3":
            id_ = input("ID do contato: ")
            email = input("Novo email: ")
            c.atualizar_email(id_, email)
        elif opcao == "4":
            id_ = input("ID do contato: ")
            telefone = input("Novo telefone: ")
            c.atualizar_telefone(id_, telefone)
        elif opcao == "5":
            id_ = input("ID do contato: ")
            c.apagar_contato(id_)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
