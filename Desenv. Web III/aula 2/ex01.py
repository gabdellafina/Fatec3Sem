import datetime

lista = ["A", "B", "C", "D"]
print (lista[2])
print (lista)

lista1 = []
lista1.append("Azul")
print (lista1)
lista1.extend(["Amarelo", "Vermelho", "Rosa", "Branco"])
print (lista1)

lista1.pop(1)
lista1.pop() #-1 também exclui o último elemento
print (lista1)

nomes = "Gil;Bia;Ana;Tina"
print (type(nomes))
print(nomes)

lista2 = nomes.split(';')
print (lista2)

data = datetime.date.today()
print(data)

datas = str(data).split('-')
print(datas)
print (f'Ano: {datas[0]}')
print (data.strftime('%d, %A'))

lista3 = ["U", "I", "E", "O", "A"]
lista3.sort()
print (lista3)
lista3.sort(reverse=True)
print(lista3)