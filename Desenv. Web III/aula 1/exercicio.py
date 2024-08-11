import random

numeros = []
def sorteio():
    i = 0
    while i < 5:
        numeros.append(random.randint(0, 10))
        i+=1
    return (numeros)

numeros = sorteio()
opcao = 1

print (f"Numeros sorteados: {numeros}")

numUser = 11

while (opcao != 0 and numUser not in numeros):
    numUser = int(input("Digite um número: \n"))
    if numUser in numeros:
        print("Encontrado")
        break
    else:
        print("Não encontrado")
    opcao = int(input("Digite 0 para sair ou qualquer outro número para continuar: \n"))