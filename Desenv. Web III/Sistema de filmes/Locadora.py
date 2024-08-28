from Filme import Filme
from Cliente import Cliente

class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []

    def adicionarFilme(self, titulo, ano, genero, disponibilidade=True):
        filme = Filme(titulo, ano, genero, disponibilidade)
        self.filmes.append(filme)
        print("Filme adicionado com sucesso!")

    def adicionarCliente(self, id, nome):
        cliente = Cliente(id, nome)
        self.clientes.append(cliente)
        print("Cliente adicionado com sucesso!")

    def alugarFilme(self, titulo, cliente_id):
        filme_encontrado = None
        for filme in self.filmes:
            if filme.titulo == titulo and filme.disponibilidade:
                filme_encontrado = filme
                break
        
        if filme_encontrado:
            filme_encontrado.disponibilidade = False
            print("Filme alugado com sucesso!")
        else:
            print("Filme indisponível ou não encontrado!")

    def listaFilmesDisp(self):
        print("Filmes disponíveis:")
        for filme in self.filmes:
            if filme.disponibilidade:
                print(filme.dadosFilme())

    def listaFilmesIndisp(self):
        print("Filmes alugados:")
        for filme in self.filmes:
            if not filme.disponibilidade:
                print(filme.dadosFilme())

    def listaClientes(self):
        print("Clientes:")
        for cliente in self.clientes:
            print(cliente.dadosCliente())
