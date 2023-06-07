lista = []
while True:
  number = int(input('Type a number: '))
  lista.append(number)
  continuation = input('Do you want to continue? Y or N ')
  if continuation[0].lower() != 'y':
    break
listaPar, listaImpar = [], []
for c in lista:
  if c % 2 == 0:
    listaPar.append(c)
  else:
    listaImpar.append(c)
print('The pair list is ', listaPar)
print('The odd list is ', listaImpar)