lista = ["Ana", "Maria", "Braga"]
dicionario = {'id':'001', 'nome': 'felipe'}

with open ('texto.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'\n\n*Lista*')
    for item in lista:
        arquivo.write(f'\n{item}')

    arquivo.write(f'\n\n*Dicionario*')
    for i, v in dicionario.items():
        arquivo.write(f'\n{i}:{v}')

    arquivo.close

with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())