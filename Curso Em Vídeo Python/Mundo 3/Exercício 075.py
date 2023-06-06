tupla = (int(input('Insert the first number: ')),
         int(input('Inserr the second number: ')),
         int(input('Insert the tirth number: ')),
         int(input('Insert the fourth number: ')))
countPair = 0
print(f'You typed {tupla}\nYou typed "9" {tupla.count(9)} times')
if 3 in tupla: print(f'3 is in {tupla.index(3)+1}th position')
else: print(f'3 isnt in your list')

print(f'The pair digited numbers was: ', end='')  
for c in tupla:
  if c % 2 == 0:
    countPair += 1
    print(c, end=' ')