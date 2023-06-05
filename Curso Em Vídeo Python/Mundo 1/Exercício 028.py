#Exercício 28

import random, time

computador = random.randint(0, 5)

print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[1;33m')
print(f'\033[1;34mVou pensar em um número entre 0 e 5, tente adivinhar....\033[1;34m')
print('\033[1;33m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[1;33m')

jogador = int(input('\033[1;36mEm que número eu pensei?{}'.format('\033[1;36m')))
if jogador > 5:
    print('\033[1;31mO número precisa ser entre 0 e 5. Não pode ser maior ou menor que esses valores.\033[1;31m')

else:
    print('\033[1;36mPROCESSADO.....\033[1;36m')
    time.sleep(3)
    if jogador == computador:
        print(f'\033[1;32mParabéns, você acertou!, você e o computador escolher o número {computador}\033[1;32m')
    else:
        print(f'\033[1;31mVocê errou :( o computador escolher o número {computador} e você escolheu o número {jogador}\033[1;31m')

print('\033[1;34mEsse foi o jogo! Espero que tenha gostado\033[1;34m')
