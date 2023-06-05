lista_idade = []
lista_genero = []
contador_pessoas = 0 #Contador que vai contar quantas pessoas foram analisadas
contador_maior_idade = 0 #Contador que vai contar quantas pessoas são +18
contador_mulheres_menor_idade = 0 #Vai contar quantas mulheres são -20 anos
contador_homens = 0 #Vai contar quantos homens foram cadastrados

while True:

    print('-'*10)
    print('CADASTRE UMA PESSOA')
    print('-'*10)

    idade = input('Idade: ')

    while idade.isnumeric() == False: #Enquanto o usuário não responder com números, esse laço vai se repetir
        idade = input('Por favor, responda com números. Idade: ')

    idade = int(idade)
    lista_idade.append(idade)

    genero = input('Gênero [M/F]: ').lower()

    while genero[0] not in 'mf':
        genero = input('Responda com "Masculino" ou "Feminino" (ou [M/F] se preferir): ')

    lista_genero.append(genero[0])

    continuar = input('Quer continuar? [S/N] ').lower()

    while continuar[0] not in 'sn':
        continuar = input('Por favor, responda com "Sim" ou "Não" (ou [S/N] se preferir): ')

    contador_pessoas += 1

    if continuar == 'n':
        break

print('='*5, 'FIM DO PROGRAMA', '='*5)

for c in range(contador_pessoas):
    if lista_idade[c] >= 18:
        contador_maior_idade += 1
        
    if lista_idade[c] < 20:
        if lista_genero[c] == 'f':
            contador_mulheres_menor_idade += 1
        
    if lista_genero[c] == 'm':
        contador_homens += 1
    
print(f'Total de pessoas com mais de 18 anos: {contador_maior_idade}')
print(f'Ao todo, temos {contador_homens} homens cadastrados ')
print(f'E temos {contador_mulheres_menor_idade} mulheres com menos de 20 anos')

"""Sei que é gambiarra, mas foi a primeira forma que pensei em fazer esse exercício"""
