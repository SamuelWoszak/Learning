#Exercicio 44
import time
preço = float(input('Qual o preço do produto? R$'))

time.sleep(1)

print("""MÉTODOS DE PAGAMENTO:
[1] - À VISTA OU CHEQUE
[2] - NO CARTÃO
[3] - PARCELADO 2X NO CARTÃO
[4] - PARCELADO 3X NO CARTÃO
[5] - CANCELAR COMPRA""")

pagamento = int(input('Qual vai ser o seu método de pagamento? '))

vista_cheque = preço - preço * 0.1
cartao = preço - preço*0.05
parcelado = preço + preço*0.2

print('-'*10)
if pagamento == 1:
    print('Você vai ter um desconto de 10% no valor do seu produto')
    print(f'Você vai pagar R${vista_cheque:.2f} já que decidiu pagar pelo método 1')

elif pagamento == 2:
    print('Você vai ter um desconto de 5% no valor do seu produto')
    print(f'Você vai pagar R${cartao:.2f} já que decidiu pagar pelo método 2')

elif pagamento == 3:
    print(f'Você vai pagar R${preço:.2f} já que vai pagar pelo método 3')

elif pagamento == 4:
    parcelas = int(input('Em quantos meses você vai pagar? '))
    print(f'Você vai pagar {parcelado/parcelas} por mes')
    print(f'Você vai pagar {parcelado:.2f} no total já que decidiu pagar pelo método 4')

elif pagamento == 5:
    print('OPERAÇÃO FINALIZADA')

else:
    print('Método inexistente.')

print('-'*10)

