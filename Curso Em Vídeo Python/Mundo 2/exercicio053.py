#Exercício 53

nome = str(input('Qual seu nome? '))

nome_sem_espaço = nome.replace(" ", "")

nome_invertido = nome_sem_espaço[::-1]

print(f'Seu nome invertido é {nome_invertido}')

if nome_invertido == nome_sem_espaço:
    print('O seu nome é um palíndromo')
else:
    print('O seu nome não é um palíndromo')