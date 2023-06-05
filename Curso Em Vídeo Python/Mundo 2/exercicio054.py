#Exercicio 54

from datetime import date

total_maior = 0
total_menor = 0

ano_atual = date.today().year

for n in range(1, 7):
    ano = int(input(f'Em que ano nasceu a {n}° pessoa? '))
    idade = ano_atual - ano
    
    if idade >= 18:
        total_maior += 1
    
    else:
        total_menor += 1

print(f'Existem {total_maior} pessoas maior de idade aqui \nExistem {total_menor} pessoas menor de idade') 