quantidade_produtos = soma = produto_caro = produto_barato = 0

while True:

    Nome_Produto = str(input('Qual o nome do produto que você quer comprar? '))

    while Nome_Produto.isalpha() == False:
        Nome_Produto = str(input('Qual o nome do produto que você quer comprar? '))

    Preço_Produto = float(input('Qual o preço desse produto? '))

    soma += Preço_Produto

    if Preço_Produto >= 100:
        produto_caro += 1

    quantidade_produtos += 1

    if quantidade_produtos == 1:
        produto_barato = Preço_Produto
        produto_barato_nome = Nome_Produto

    elif Preço_Produto < produto_barato:
        produto_barato = Preço_Produto
        produto_barato_nome = Nome_Produto

    resposta = ' '

    while resposta[0] not in 'sn':
        resposta = str(input('Você quer continuar comprando produtos? ')).lower()

    if resposta == 'n':
        break

print(f'O total gasto na compra foi {soma}')
print(f'Você comprou {produto_caro} produtos que custam mais de 100 reais')
print(f'O produto mais barato que você comprou custa {produto_barato} e foi o {produto_barato_nome}')

