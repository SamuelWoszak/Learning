import time

n1 = int(input('Escolha o primeiro valor: '))
n2 = int(input('Escolha o segundo valor: '))
    

option = 0

while option != 5:
    print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR!""")

    option = int(input('Escolha a opção:  '))
    print('-'*10)

    if option == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
        print('-=-=-=-'*10)
    
    if option == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1*n2}')
        print('-=-=-=-'*10)

    
    if option == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('-=-=-=-'*10)

        if n1 < n2:
            print(f'{n2} é maior que {n1}')
            print('-=-=-=-'*10)

        if n1 == n2:
            print(f'{n1} é igual a {n2}')
            print('-=-=-=-'*10)      

    if option == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número:'))
        print('-='*10)


    if option == 5:
        print('Volte sempre!')
        print('-=-=-=-'*10)

    if option > 5 or option < 1:
        print('Opção inválida. Tente novamente.')
        
    time.sleep(1)
    

print('Fim do programa')