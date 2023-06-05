g = str(input('Qual seu gênero? [M/F] ')).upper().strip()

while g[0] not in 'FM':
    g = str(input('Dados inválidos. Insira novamente: ')).strip().upper()

print('Obrigado!')