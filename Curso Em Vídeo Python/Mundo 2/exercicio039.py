#Exercício 39

import datetime

#Variáveis 

ano = int(input('Em que ano você nasceu?'))
idade = int(datetime.datetime.now().year - ano)

if idade > 18:      
    print(f'Você devia ter se alistado há {idade - 18} anos atrás')
    
elif idade == 18:
    print('Você deve se alistar no exército nesse ano')
    
else:
    print(f'Você vai se alistar no exército em {ano + 18}')


