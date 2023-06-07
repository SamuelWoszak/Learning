lista = []
for c in range(1, 6):
  number = int(input(f'Type the value of the {c} position: '))
  lista.append(number)

print(f'You typed {lista}')
print(f'The highest one is {max(lista)}\nThe smallest one is {min(lista)}')