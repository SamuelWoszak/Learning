#Exercício 20

import random

a1 = str(input('Escolha o primeiro aluno: '))
a2 = str(input('Escolha o segundo aluno: '))
a3 = str(input('Escolha o terceiro aluno: '))
a4 = str(input('Escolha o quarto aluno: '))
lista = [a1,a2,a3,a4]
esolhidos = random.shuffle(lista)

print('Os alunos escolhidos foram')
print(f'{lista} ,nessa ordem')
