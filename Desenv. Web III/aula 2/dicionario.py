dicionario = {'Gabriela':'Aluna', 'Maria':'Professora'}
print (dicionario)

dicionario ['Braga'] = "funcionario"
print (dicionario)

del dicionario ['Braga']
print (dicionario)

for c, v in dicionario.items():
    print(f'\n Chave: {c}')
    print (f' Valor: {v}')

