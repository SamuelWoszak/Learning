#Exercicio 52
#Exercicio 52

n = int(input('Escolha um número: '))
total = 0


for v in range(1, n+1):
    if n % v == 0:
        print('\033[33m', end='')
        total += 1
    
    else:
        print('\033[31m', end='')
    
    print(f'{v}', end=' ')

print(f'\033[34m O número {n} é divisivel {total} vezes')

if total == 2 
    print('O número é primo')

else:
    print('O número não é primo')

