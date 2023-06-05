#Exercício 29

carro = float(input('Quantos km por hora você estava andando com o seu carro na estrada? '))

if carro > 80:
    print(f'PARADO! Você está andando a uma velocidade maior que 80km/h, \nVocê deverá pagar uma multa de R${(carro - 80)*7:.2f}')
else:
    print(f'Você está na velocidade adequada')

print('------------')
