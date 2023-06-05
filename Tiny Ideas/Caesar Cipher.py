#Make a Caesar Cipher with an input key

frase = input('Phrase to ciptograph ')
chave = int(input('The Key: ')) % 26
alfabeto = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alfabeto2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
FraseCriptografada = ''
for c in frase:
  if c in alfabeto:
    c = alfabeto[alfabeto.find(c) + chave]
  elif c in alfabeto2:
    c = alfabeto2[alfabeto2.find(c) + chave]
  else:
    pass
  FraseCriptografada = FraseCriptografada + c

print(FraseCriptografada)
