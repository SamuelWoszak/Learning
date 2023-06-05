escolha = 'S'
soma = quantidade = média = maior = menor = 0

while escolha in 'Ss':

    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1

    if quantidade == 1:
        maior = menor = n

    else:

        if n > maior:
            maior = n

        if n < menor:
            menor = n

    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]


print(f'A quantidade de termos que você usou foi de {quantidade}')
print(f'A soma entre todos os termos é igual a {soma}')
print(f'O menor número digitado foi o {menor}')
print(f'O maior número digitado foi o {maior}')
print(f'A média entre todos os números é igual a {soma/quantidade:.2f}')