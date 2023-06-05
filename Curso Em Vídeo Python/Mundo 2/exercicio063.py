print('-- Sequência de Fibonacci --')

n = int(input('Digite quantos termos você quer: '))

n1 = 0
n2 = 1

quant = 0

tot = 0

while n != 0:
    tot += n
    
    while quant < tot:
        n3 = n1 + n2

        print(n1)

        n1 = n2
        n2 = n3
        quant += 1
    
    n = int(input('Quantos termos você quer? '))

print(' -> FIM')