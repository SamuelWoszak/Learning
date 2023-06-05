import random, time

computerop = random.randint(1, 10)
print('Sou o computador, e seu adversário')
print('Acabei de pensar em um número de 0 a 10')
print('Será que você consegue adivinhar em que número eu pensei?')

player = int(input('Qual o seu palpite? '))

palpite = 1

if player < 1 and player > 10:
    print('Por favor, insirá um número válido!') 

while player != computerop:
    if player > computerop:
        print('\033[31;1mO número sorteado é menor que o seu número escolhido')
        player = int(input('Escolha outro número!\033[31;1m'))
        palpite += 1
        
    elif player < computerop:
        print('\033[31;1mO número sorteado é maior que o seu número escolhido')
        player = int(input('Escolha outro número!\033[31;1m'))
        palpite += 1

print(f'\033[32;1mCORRETO! Você e o computador escolheram o número {computerop}\033[32;1m')

if palpite == 1:
    print(f'\033[36;1m Você precisou de 1 chance para acertar')

else:
    print(f'\033[36;1m Você precisou de {palpite} chances para acertar')