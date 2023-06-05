#Exercicio 50

s = 0

for c in range(1, 7):
    n = int(input(f'Escolha o {c}° número: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma entre os números pares entre esses números escolhidos vai ser igual a {s}')
