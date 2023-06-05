lista = []
for c in range(1, 6):
    numero = int(input('Coloque o número '))
    lista.append(numero)
maximo = max(lista)
counter = counter2 = 0
lista2 = lista
if lista.count(maximo) > 1:
    print(f'{maximo} foi o maior número e ', end='')
    for c in lista:
        counter += 1
        if c == max(lista2):
            print(f'{counter}, ',end='')        
            counter2 += 1
        if counter2 + 1 == lista2.count(maximo):
            print(f'{counter + 1} são as posições dele!')  
            break      

else:
    print(f'{max(lista)} foi o maior número e foi o {lista.index(max(lista))+1} número que digitou!')
    
#Nota: O exercício inicial não utiliza a ideia de que pode haver mais de um número máximo digitado, ele apenas retorna como "x"... "y"..., sendo x e y as posições do máximo
#citado. 
