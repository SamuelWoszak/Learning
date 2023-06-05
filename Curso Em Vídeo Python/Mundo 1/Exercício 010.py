#Exercício 10

valor = float(input('Quanto você tem? R$'))
dolar = float(valor/5.75)
euros = float(valor/6.74)

print('com R${:.2f} você pode comprar US${:.2f} dólares e {:.2f} euros. '.format(valor, dolar, euros))
