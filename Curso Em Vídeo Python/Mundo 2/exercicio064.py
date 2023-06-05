n = int(input('Digite um número [digite 999 para parar o processo]: '))
total = 0
soma = 0


while n != 999:
    
    n = int(input('Digite outro número novamente [digite 999 para parar o processo]:'))
    soma += n
    total += 1

print(f'Você digitou {total} termos')
print(f'A soma entre todos esses termos é igual a {soma - 999}')