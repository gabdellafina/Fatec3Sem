import datetime

class Pessoa:
    def __init__(self, _nome, _idade):
        self.nome = _nome
        self.idade = _idade

    def dados(self):
        print(f"Bem vindo {self.nome}, você tem {self.idade} anos")

    def ano_nasc(self):
        data = datetime.datetime.now()
        ano = data.year
        return ano - self.idade
    

# p1 = Pessoa("Mariana", 21)
# print(p1.nome, p1.idade)

# p1.dados()
# print(f"Nasceu em: {p1.ano_nasc()}")