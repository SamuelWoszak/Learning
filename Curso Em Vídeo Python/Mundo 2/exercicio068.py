import random

print('-'*10)
print('Vamos jogar Par ou Ímpar!')
print('-'*10)

contador = contador_vitoria = 0 #Contador para ver quantas vezes o usuário jogou o jogo

while True:
    
    player_num = input('Escolha seu número: ')

    while player_num.isnumeric() == False: #Se o usuário digitar algo que não seja número, o programa o forçará a digitar números
        
        player_num = input('Por favor, insira apenas números ')

    player_num = int(player_num) #Transforma o número escolhido em int()

    escolha = str(input('Par ou Ímpar? ')).lower()

    while escolha[0] not in 'pií':
        escolha = str(input('Por favor, escolha corretamente. Par ou ímpar? '))
    
    if escolha == 'í':
        escolha = 'i'

    if escolha == 'p':
        escolha_computador = 'i'

    if escolha == 'i' :
        escolha_computador = 'p'

    computador_num = random.randint(0, 10)

    soma = computador_num + player_num

    if soma % 2 == 0:
        resultado = 'p'

    elif soma % 2 != 0:  
        resultado = 'i'

    if resultado == escolha[0]:
        print(f'Você ganhou! O computador escolheu {computador_num} e você {player_num}, somando {soma} total.')
        contador += 1
        contador_vitoria += 1

    if resultado != escolha[0]:
        print(f'Você perdeu :( O computador escolheu o número {computador_num} e você {player_num}, somando {soma} no total')
        contador += 1
        break

    print('-'* 10)

print('-'*10)
print(f'Game Over. Você jogou esse jogo {contador} vezes, e conseguiu vencer {contador_vitoria} vezes!')
