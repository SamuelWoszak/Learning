#Exercício 14

km = float(input('Quantos km você andou com o carro? '))
dia = int(input('Você usou o carro por quantos dias? '))

dx = dia*60
kmx = km*0.15

print('Você usou o carro por {} dias, sabendo que o preço diário é de 60 reais, você deve pagar R${} pela diária'.format(dia, dx))
print('Você andou {}km com o carro, sabendo que o preço de cada km andado é de R$0.15, você vai ter que pagar R${}.'.format(km, kmx))
print('Você deve pagar R${} no total.'.format(kmx+dx))
