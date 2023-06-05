peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui a sua altura: '))
imc = peso/altura**2

print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')

elif imc >= 25 and imc < 30:
    print('Você está no sobrepeso')

elif imc >= 30 and imc < 40:
    print('Você está na obesidade ')

else:
    print('Você está na obesidade mórbida')