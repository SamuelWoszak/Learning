print('BANCO BINGUS')

dinheiro = int(input('Quantos reais você quer gastar? '))

while dinheiro < 0:
    dinheiro = int(input('Por favor, insira corretamente '))

ced50 = ced20 = ced10 = ced5 = ced2 = moeda1 = 0

while dinheiro > 0:

    if dinheiro >= 50:
        ced50 += 1
        dinheiro -= 50
    
    elif dinheiro >= 20 and dinheiro < 50:
        ced20 += 1
        dinheiro -= 20
    
    elif dinheiro >= 10 and dinheiro < 20:
        ced10 += 1
        dinheiro -= 10
    
    elif dinheiro >= 5 and dinheiro < 10:
        ced5 += 1
        dinheiro -= 5
    
    elif dinheiro >= 2 and dinheiro < 5:
        ced2 += 1
        dinheiro -= 2
    
    elif dinheiro == 1:
        moeda1 += 1
        dinheiro -= 1
    
if ced50 > 0:
    print(f'Você usou {ced50} notas de R$50')

if ced20 > 0:
    print(f'Você usou {ced20} notas de R$20')

if ced10 > 0:
    print(f'Você usou {ced10} notas de R$10')

if ced5 > 0:
    print(f'Você usou {ced5} notas de R$5')

if ced2 > 0:
    print(f'Você usou {ced2} notas de R$2')

if moeda1 > 0:
    print(f'Você usou {moeda1} moeda de R$1')

