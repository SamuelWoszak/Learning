#Exercício 19

import random 

n1 = str(input('Escolha o primeiro aluno: '))
n2 = str(input('Escolha o segundo aluno: '))
n3 = str(input('Escolha o terceiro aluno: '))
n4 = str(input('Escolha o quarto aluno: '))
lista = n1,n2,n3,n4
escolhido = random.choice(lista)

print('O aluno escolhido foi o {}'.format(escolhido))
