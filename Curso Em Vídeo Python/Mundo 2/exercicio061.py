a1 = int(input('Insira o primeiro termo dessa p.a.: '))
r = int(input('Insitra a razão dessa p.a.'))

quant = 1

while quant <= 10:
    pa = a1 + r
    print(quant,'° ', ' -> ', a1)
    a1 = pa
    quant += 1