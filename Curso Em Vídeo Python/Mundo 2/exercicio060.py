n1 = int(input('Fatorial de: '))
c = n1
tot = 1

while c > 0:
    
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    tot*= c
    c -= 1
    
    

print(f'{tot}')





