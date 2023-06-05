import time

print('-=' * 20)

reta1 = float(input('Insira o valor da primeira reta: '))
reta2 = float(input('Insira o valor da segunda reta: '))
reta3 = float(input('Insira o valor da terceira reta: '))

print('-=' * 20)

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível formar um triângulo ', end='')
    time.sleep(1)
    if reta1 == reta2 and reta2 == reta3:
        print('É possível formar um triângulo equilátero')

    elif reta2 == reta1 and reta2 != reta3 or reta2 == reta3 and reta3 != reta1 or reta1 == reta3 and reta3 != reta2:
        print('É possível formar um triângulo isóceles')
    
    else:
        print('É possível formar um triângulo escaleno')
    


else:
    print('Não é possível formar um triângulo')
print('Finalizado')