#Exercício 34 

salario = float(input('Qual o valor do salário?'))

if salario >= 1250:
    print(f'O aumento do salário será de 10%, então, o funcionário receberá {salario + salario*0.1}')

else:
    print(f'O aumento do salário será de 15%, então, o funcionário receberá {salario + salario*0.15}')
