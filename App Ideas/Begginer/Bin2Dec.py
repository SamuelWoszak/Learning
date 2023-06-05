#This one needs to create a program that converts Binary to Decimal

number = input('Insert a bin number: ')
counter = total = 0
for c in number:
  if c == '1':
    total += 2**counter
  counter += 1
  
print(total)
  
