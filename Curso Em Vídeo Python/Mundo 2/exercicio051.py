#Exercicio 51

print('-'*10)
print('Calculadora de P.A.')
print('-'*10)

termo1 = int(input('Insira o primeiro termo dessa P.A.'))
Razao = int(input('Insira a RAZÃO dessa P.A.'))

print('Os 10 primeiros termos dessa P.A. são:')
for n in range(1, 11):
    pa = termo1 + Razao*(n - 1)
    print('-', pa)