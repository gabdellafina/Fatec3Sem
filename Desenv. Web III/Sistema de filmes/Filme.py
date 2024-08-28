class Filme:
    def __init__(self, _titulo, _ano, _genero, _disponibilidade):
        self.titulo = _titulo
        self.ano = _ano
        self.genero = _genero
        self.disponibilidade = _disponibilidade

    def dadosFilme(self):
        print(f"Título: {self.titulo}\nAno: {self.ano}\nGenero: {self.genero}\nDisponibilidade: {self.disponibilidade}")