#Exercicio 36

casa = float(input('Qual o valor da casa que você vai comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
tempo = int(input('Quantos anos você vai pagar? '))
mes = tempo*12
prestação = casa/mes


if prestação > salario*0.31:
    print(f'Você não pode pagar essa prestação, o valor da prestação é maior que 30% do seu salário.\n Mas o custo seria igual a {prestação:.2f}')

else:
    print(f'Você vai precisar gastar R${prestação:.2f} por mês, durante esse tempo')
