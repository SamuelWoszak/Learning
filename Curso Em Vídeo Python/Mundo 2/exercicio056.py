#Exercicio 56

m = 0 #Masculino
f = 0 #Feminino

somaidade = 0 #soma de todas as idades
maioridadehomem = 0 #o homem mais velho
nomemaisvelho = '' #o nome do homem mais velho
totm20 = 0 #total de mulheres que tem menos de 20 anos

for r in range(1, 5):
    print('-----'*10)
    print(f'{r}° PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    
    if r == 1 and Sexo in 'Mm':
        nomemaisvelho = nome
        maioridadehomem = idade
    
    if Sexo in 'Mm' and maioridadehomem < idade:
        maioridadehomem = idade
        nomemaisvelho = nome

    if Sexo in 'Ff' and idade < 20:
        totm20 += 1


mediaidade = somaidade/4

print(f'A media de idade do grupo é {mediaidade:.2f}')
print(f'O homem mais velho tem {maioridadehomem} e ele se chama {nomemaisvelho.capitalize()}')
print(f'A quantidade de mulheres que tem menos da 20 anos é igual a {totm20}')
