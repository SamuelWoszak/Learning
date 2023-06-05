#Exercício 26

frase = str(input('Digite uma frase: ')) .strip().lower()

print('A sua frase tem {} letras A'.format(frase.count('a')))
print('A primeira vez que a letra A aparece é na posição {}'.format(frase.find('a')+1))
print(f'A ultima vez que a letra A aparece na frase é na posição {frase.rfind("a")+1 - frase.count(" ")}')
