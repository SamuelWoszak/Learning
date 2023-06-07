expression = input('Type the expression! ')
countP = []
for c in expression:
  if c == '(' or c == ')':
    countP.append(c)
if countP.count('(') == countP.count(')'):
  print('Valid expression!')
else:
  print('Invalid expression!')