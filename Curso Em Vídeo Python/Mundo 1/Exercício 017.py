#Exercício 17

from math import radians, sin, cos, tan

ang = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O valor do ângulo é igual a {}, então, o SENO vai ser igual a {:.2f}'.format(ang, seno))
print('O valor do cosseno é igual a {:.2f}'.format(cos))
print('O valor da tangente é igual a {:.2f}'.format(tan))
