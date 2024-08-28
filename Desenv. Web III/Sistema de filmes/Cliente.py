class Cliente:
    def __init__(self, _id, _nome):
        self.id = _id
        self.nome = _nome

    def dadosCliente(self):
        print(f"ID: {self.id}\nNome: {self.nome}")