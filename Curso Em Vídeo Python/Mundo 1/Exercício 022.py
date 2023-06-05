#Exercício 022

n1 = str(input('Digite o seu nome ')).strip()
print('O seu nome com todas as letras maiúsculas é {}'.format(n1.upper()))
print('O seu nome com todas as letras minúsculas é {}'.format(n1.lower()))
print('O seu nome ao todo tem {} letras'.format(len(n1)-n1.count(' ')))

#print('O seu primeiro número tem {} letras'.format(n1.find(' '))) é uma opção mas eu nao gostei
 
n1sep = n1.split()

print('O seu primeiro nome é {} e ele tem {} letras'.format(n1sep[0], len(n1sep[0])))
