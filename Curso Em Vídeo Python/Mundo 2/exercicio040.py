#Exercício 40

nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2)/2

if media < 0:
    print('Essa média não existe.')

elif media > 0 and media <= 5:
    print(f'A sua média foi {media:.1f}. Você está de REPROVADO')

elif media >= 5 and media < 7:
    print(f'A sua média foi {media:.1f}. Você está de recuperação')

else:
    print(f'A sua nota foi {media:.1f}. APROVADO')