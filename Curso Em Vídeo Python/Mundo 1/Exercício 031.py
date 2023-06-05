#Exercício 31

distancia = int(input('Quantos km você andou com o seu carro? '))

if distancia <= 200:
    print('Você deverá pagar R${} pela distância percorrida'.format(distancia*0.5))
else:
    print(f'Você deverá pagar R${distancia*0.45} pela distância percorrida.')
