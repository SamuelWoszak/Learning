#Exercício 41

idade = int(input('Qual a sua idade para ingressar na natação? '))

if idade < 0:
    print('Solução inexistente. ')

elif idade <= 9:
    print('categoria MIRIM')

elif idade <= 14 and idade > 9:
    print('Categoria INFANTIL')

elif idade <= 19 and idade > 14:
    print('Categoria JUNIOR')

elif idade <= 25 and idade > 19:
    print('Categoria SÊNIOR')

else:
    print('Categoria Master')