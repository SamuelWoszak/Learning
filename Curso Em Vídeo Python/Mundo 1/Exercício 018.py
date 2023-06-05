#Exercício 18

import math

ang = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))

cos = math.cos(math.radians(ang))
print('O valor de cosseno do ângulo de {}° é igual a {:.2f}'.format(ang, cos))

tang = math.tan(math.radians(ang))
print('O valor da tangete do ângulo de {}° é igual a {:.2f}'.format(ang, tang))
