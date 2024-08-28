from Locadora import Locadora
import sys

class Main:
    def __init__(self):
        self.locadora = Locadora()

    def menu(self):
        print("---------------------")
        print("Menu da Locadora:")
        print("1- Adicionar filme")
        print("2- Adicionar cliente")
        print("3- Alugar filme")
        print("4- Listar filmes disponíveis")
        print("5- Listar filmes alugados")
        print("6- Listar clientes")
        print("7- Sair")
        print("---------------------")

    def escolha(self):
        while True:
            self.menu()
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                titulo = input("Digite o nome do filme: ")
                ano = int(input("Digite o ano do filme: "))
                genero = input("Digite o gênero do filme: ")
                self.locadora.adicionarFilme(titulo, ano, genero)
            elif opcao == 2:
                id = int(input("Digite o ID do cliente: "))
                nome = input("Digite o nome do cliente: ")
                self.locadora.adicionarCliente(id, nome)
            elif opcao == 3:
                titulo = input("Digite o título do filme a ser alugado: ")
                cliente_id = int(input("Digite o ID do cliente: "))
                self.locadora.alugarFilme(titulo, cliente_id)
            elif opcao == 4:
                self.locadora.listaFilmesDisp()
            elif opcao == 5:
                self.locadora.listaFilmesIndisp()
            elif opcao == 6:
                self.locadora.listaClientes()
            elif opcao == 7:
                sys.exit()
            else:
                print("Opção inválida!")

    def main(self):
        self.escolha()

if __name__ == "__main__":
    main = Main()
    main.main()
