#Pedra Papel E Tesoura
#Arquivo.py

import random, time
pedra = 1
papel = 2
tesoura = 3
escolhas = [pedra, papel, tesoura]
print("""PEDRA = 1
PAPEL = 2
TESOURA = 3""")

jogador = int(input('O que você vai escolher?'))
computador = random.choice(escolhas)
if jogador > 3:
    print('Você selecionou um número que ultrapassa os limites.')


elif jogador == computador:
    print('E O RESULTADO FOI....')
    time.sleep(2)
    print('EMPATE! Vocês escolheram os mesmos itens')

#DERROTA DO JOGADOR

elif jogador == tesoura and computador == pedra:
    print('E O RESULTADO FOI....')
    time.sleep(2)
    print('{} Você perdeu {} O computador escolheu PEDRA e você escolheu TESOURA'.format('\033[31;1m','\033[31;1m' ))

elif jogador == pedra and computador == papel:
    print('E O RESULTADO FOI....')
    time.sleep(2)
    print('{} Você perdeu {} O computador escolheu PAPEL e você escolheu PEDRA'.format('\033[31;1m','\033[31;1m' ))

elif jogador == papel and computador == tesoura:
    print('E O RESULTADO FOI....')
    time.sleep(2)
    print('{} Você perdeu {} O computador escolher TESOURA e você papel'.format('\033[31;1m','\033[31;1m' ))

#VITÓRIAS DO JOGADOR

elif jogador == papel and computador == pedra:
    print('E O RESULTADO FOI...')
    time.sleep(2)
    print('{} Você ganhou! {} O computador escolher PEDRA e você PAPEL'.format('\033[32;1m','\033[32;1m'))

elif jogador == pedra and computador == tesoura:
    print('E O RESULTADO FOI...')
    time.sleep(2)
    print('{} Você ganhou! {} O computador escolher TESOURA e você PEDRA'.format('\033[32;1m','\033[32;1m'))

elif jogador == tesoura and computador == papel:
    print('E O RESULTADO FOI...')
    time.sleep(2)
    print('{} Você ganhou! {} O computador escolher PAPEL e você TESOURA'.format('\033[32;1m','\033[32;1m'))
