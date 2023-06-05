número = 0
soma = 0
quantidade = 0

while número != 999:
    número = int(input('Digite um valor [Digite 999 para parar]: '))
    
    if número == 999:
        break
    
    quantidade += 1
    soma += número


print(f'Você digitou {quantidade} números, e a soma de todos eles é igual a {soma}')
