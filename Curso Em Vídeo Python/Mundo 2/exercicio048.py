#Exercicio 48

s = 0
quant = 0

print('   '*10)
print('A soma entre todos os números ímpares entre 0 e 500 que são multiplos de 3:')
print('   '*10)


for c in range(0, 501):
    if c % 2 != 0:
        if c % 3 == 0 :
            print(c)
            s += c
            quant += 1

print('Esses foram os números múltiplos de 3 que ficam entre 0 e 500')
print('     ')
print(f'A soma entre todos esses número é igual a {s}, e possui {quant} valores ímpares e múltiplos de 3 entre 0 e 500')
