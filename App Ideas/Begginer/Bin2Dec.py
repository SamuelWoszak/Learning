#This one needs to create a program that converts Binary to Decimal

number = input('Insert a bin number: ')
counter = total = 0
for c in number:
  if c == '1':
    total += 2**counter
  counter += 1
  if c != '1' or c != '0':
    print('You put sometihng different than 0 or 1, please insert only 1 or 0!')
    quit()
print(total)
