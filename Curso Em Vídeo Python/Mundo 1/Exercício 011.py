#Exercício 11

larg = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))
área = alt*larg
litro = área/2

print('A dimensão da sua parede é igual a {}m²'.format(área))
print('Para pintar a parede você precisa de {}L de tinta.'.format(litro))
