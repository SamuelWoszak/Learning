#Exercício 33

a = int(input('Diga o valor do número: '))
b = int(input('Diga o valor do número: '))
c = int(input('Diga o valor do número: '))

menorvalor = a
maiorvalor = b

if b<a and b<c:
    menorvalor = b

if c<a and c<b:
    menorvalor = c

if c>a and c>b:
    maiorvalor = c

if a>b and a>c:
   maiorvalor = a

print(f'O menor valor foi {menorvalor} \nO maior valor foi o {maiorvalor}')
