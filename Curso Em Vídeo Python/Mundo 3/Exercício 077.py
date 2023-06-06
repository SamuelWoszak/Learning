palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = 'AEIOU'
for c in range(0, len(palavras)):
  print(f'\nNa palavra {palavras[c]} temos as vogais ', end ='')
  for i in palavras[c]:
    if i in vogais:
      print(i, end='')