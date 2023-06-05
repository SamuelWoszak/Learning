a1 = int(input('Insira o primeiro termo dessa p.a.: '))
r = int(input('Insitra a razão dessa p.a.'))

quant = 1
continuar = 10
tot = 1

while continuar != 0:
    
    tot += continuar
    
    while quant <= tot:
        an = a1 + r*(quant - 1)
        quant += 1
        print(an)

    
    continuar = int(input('Quantos termos a mais você quer? Digite [0] para interromper o programa '))
    