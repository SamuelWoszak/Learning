#See if a word is anagram of another one

palavra = input('Insira aqui a palavra para analisar ')
palavra2 = input(f'Insira aqui a outra palavra para ver se {palavra} é anagrama dessa que você deseja conferir ')
if sorted(palavra.lower()) == sorted(palavra2.lower()):
  print('São anagramas!')
else:
  print('Não são anagramas ')
