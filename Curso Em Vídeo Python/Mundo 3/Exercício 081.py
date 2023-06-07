lista = []
while True:
  number = int(input('Type a number: '))
  lista.append(number)
  continuation = input('Do you want to continue? Y or N ')
  if continuation[0].lower() != 'y':
    break
print(f'You typed {len(lista)} elements\nThe values in decrescent ordem are {sorted(lista)[::-1]}')
if 5 in lista:
  print('5 is in the list!')
else:
  print('5 isnt in the list')