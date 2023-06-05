#Exercicio 47
import time

print('-'*10)
print('Esses são os números pares entre 0 e 50:')
print('-'*10)

time.sleep(3)

for c in range(0, 51, 2):
    time.sleep(0.3)
    print(c, end=' -> ')