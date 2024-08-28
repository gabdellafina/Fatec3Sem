from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, _nome, _idade, _matricula, _curso):
        super().__init__(_nome, _idade)
        self.matricula = _matricula
        self.curso = _curso

    def dados(self):
        print(f"Olá aluno {self.nome}, você tem {self.idade} anos")

a1 = Aluno("Gab", 19, "001", "DSM")
a1.dados()
print(f"Nasceu em: {a1.ano_nasc()}")
print(f"Você faz o curso de {a1.curso} e sua matrícula é {a1.matricula}")

a2 = Aluno("Maria", 12, "65", "DSJO")

exclui = input("Digite a matrícula que deseja excluir: ")

del 