#agenda
import sys

agenda = {}

def exibir_menu():
    print("Menu:")
    print("1. Adicionar novo contato")
    print("2. Exibir contatos existentes")
    print("3. Buscar contato")
    print("4. Sair")
        
    opcao = input("Escolha uma opção: ")
        
    if opcao == "1":
        addContato()
    elif opcao == "2":
        exibirContatos()
    elif opcao == "3":
        buscarContato()
    elif opcao == "4":
        sys.exit()
    else:
        print("Opção inválida. Tente novamente.")

def addContato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    agenda[nome] = telefone
    print ("Contato adicionado com sucesso!\n\n")
    exibir_menu()

def exibirContatos():
    for n, t in agenda.items():
        print (f'Nome: {n} \nTelefone: {t}')
    print ("\n\n")
    exibir_menu()

def buscarContato():
    nomeBuscar = input("Digite o nome que deseja buscar: ")
    if nomeBuscar in agenda:
        print(f'O número de {nomeBuscar} é: ', agenda[nomeBuscar], '\n\n')
    else:
        print("Contato inexistente \n\n")
    exibir_menu()

exibir_menu()