#Exercício 016

import math 

n1 = float(input('Escolha o valor da medida do cateto adjascente: '))
n2 = float(input('Escolha o valor da medida do cateto oposto: '))
hip = math.hypot(n1, n2)

print('O valor escolhido para os catetos adjascente e oposto, respectivamente foram {} e {}. O valor da hipotenusa é {:.2f}.'.format(n1, n2, hip))
