lista = []
for c in range(0, 4):
  number = int(input('Type a number: '))
  if len(lista) == 0:
    lista.append(number)
  else:
    if number >= max(lista):
      print(f'Adding in the end of the list ')
      lista.insert(0, number)
    elif number < min(lista):
      print(f'Adding to the start of the list')
      lista.insert(len(lista), number)
    else:
      for c in range(1, len(lista)):
        if lista[c-1] > number >= lista[c]:
          print(f'Adding to the {c + 1} position')
          lista.insert(c, number)
        
print(lista)