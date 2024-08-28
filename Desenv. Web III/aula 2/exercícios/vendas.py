# 2. Criar um programa em Python que leia um arquivo de texto com dados de vendas (data, produto, quantidade, preco_unitario), em seguida, gere um relatório detalhado com base nesses dados, que mostre o total de vendas por produto, o total de vendas por dia e o total geral de vendas. O relatório deve ser armazenado em um novo arquivo de texto, relatorio.txt, e apresentado na tela.

dados = []


with open ('vendas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        if linha.strip():
            dado = linha.strip().split(',')
            data = dado[0]
            produto = dado[1]
            quantidade = int(dado[2])
            preco_unitario = float(dado[3])
        
            dados.append([data, produto, quantidade, preco_unitario])

        print(data, produto, quantidade, preco_unitario)
            
with open ('relatorio.txt', 'w', encoding='utf-8') as relatorio:
    for dado in dados:
        data = dado[0]
        produtos = dado[1]
        quantidade = dado[2]
        preco_unitario = dado[3]
        total = quantidade * preco_unitario
        relatorio.write(f'Data: {data}, Produtos: {produtos}, Quantidade: {quantidade}, Preço unitário: {preco_unitario}, Total: {total}\n')

