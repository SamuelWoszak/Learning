lista = []
while True:
  numero = int(input('Type a number: '))
  if lista.count(numero) >= 1: print('Duplicate numer, will not add this to the list. ')
  else: lista.append(numero)
  escolha = str(input('Do you want to continue? Type Y or N '))
  if escolha.lower() != 'y': break  
print(f'You typed {lista}')