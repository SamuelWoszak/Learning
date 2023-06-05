#Exercicio 55
maiorp = 0
menorp = 0

for i in range(1, 7):
    p = float(input(f'Qual o peso da {i}° pessoa? '))
    if p == 1:
        maiorp = p
        menorp = p

    else:
        if p > maiorp:
            maiorp = p

        if p < menorp:
            menorp = p        

print(f'O menor peso é {menorp}')
print(f'O maior peso é {maiorp}')