#Exercício 038

n1 = float(input('Escolha o primeiro número: '))
n2 = float(input('Escolha o segundo número: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo ({n2})')

elif n1 < n2:
    print(f'O segundo valor ({n2}) é maior que o primeiro ({n1})')

else:
    print('Eles são iguais')