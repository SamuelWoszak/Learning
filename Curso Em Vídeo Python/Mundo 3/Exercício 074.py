from random import randint

tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end='')
for c in tupla:
  print(c, end= ' ')
print(f'\nO máximo da tupla foi {max(tupla)}')
print(f'O mínimo da tupla foi {min(tupla)}')