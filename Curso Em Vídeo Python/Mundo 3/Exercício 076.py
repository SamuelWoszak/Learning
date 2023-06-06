informacoes = ('Lápis', 2.00, 'Borracha', 2.50, 'Caderno', 16.00,
               'Estojo', 25.00, 'Transferidor', 5.00, 'Compasso', 10.00,
               'Mochila', 125.00, 'Canetas', 22.50, 'Livro', 35.00)

counter = 0
print('-' * 31)
print(' ' * 8, 'LISTA DE PREÇO')
print('-' * 31)
for c in range(0, len(informacoes)):
  if c % 2 == 0:
    print(f'{informacoes[c]:.<23}', end="")
  else:
    print(f'R${informacoes[c]:>6.2f}')