#Exercício 35

print('-=' * 20)
reta1 = float(input('Insira o valor da primeira reta: '))
reta2 = float(input('Insira o valor da segunda reta: '))
reta3 = float(input('Insira o valor da terceira reta: '))
print('-=' * 20)

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo ')

else:
    print('Não é possível formar um triângulo')

print('--------------Finalizado--------------')
