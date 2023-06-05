list_used_nums = []

while True:

    num = int(input('Digite aqui o número que você quer para fazer a tabuada [Digite um número negativo para interomper] '))

    if num < 0:
        
        break
    
    list_used_nums.append(num)

    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
        
    print('-'*10)
    
    
print(f'Você usou as tabuadas dos números {list_used_nums}')
list_used_nums.sort()
print(f'Caso queira os números digitados em ordem crescente: {list_used_nums}')
