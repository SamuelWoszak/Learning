from math import sqrt
from fractions import Fraction

def InputABC():
  a = float(input('Insert the value of "a": '))
  b = float(input('Insert the value of "b": '))
  c = float(input('Insert the value of "c": '))

  return a, b, c

def DiscriminantPositive(a, b, c):
  delta = b ** 2 - 4 * a * c
  if sqrt(delta) == int(sqrt(delta)):
    x1 = Fraction(f'{(-b + sqrt(delta))/(2 * a).limit_denominator()}')
    x2 = Fraction(f'{(-b - sqrt(delta))/(2 * a).limit_denominator()}')
  else:
    if delta % 4 == 0 or (delta // 4) % (a ** 2) or delta % (a ** 2) == 0:
      x1 = f'{Fraction(-b/(2 * a)).limit_denominator()} + √({Fraction(delta/(4 * (a ** 2))).limit_denominator()})'
      x2 = f'{Fraction(-b/(2 * a)).limit_denominator()} - √({Fraction(delta/(4 * (a ** 2))).limit_denominator()})'
    
  return f'Your roots are \nx1 = {x1}\nx2 = {x2}'

def DiscriminanteNule(a, b):
  x1 = Fraction(f'{-b/(2 * a)}')
  return f'Your discriminant is equal 0, so you have a root with multiplicity 2 and this is \nx1 = {x1}'

def DiscriminantNegative(a, b, c):
  delta = b ** 2 - 4 * a * c
  if sqrt(abs(delta)) == int(sqrt(abs(delta))):
    x1 = f'{Fraction(-b/(2 * a)).limit_denominator()} + i({sqrt(Fraction(delta/(4 * (a ** 2))))})'
    x2 = f'{Fraction(-b/(2 * a)).limit_denominator()} - i({sqrt(Fraction(delta/(4 * (a ** 2))))})'
  else:
    x1 = f'{Fraction(-b/(2 * a)).limit_denominator()} + i√({Fraction(abs(delta)/(4 * (a ** 2))).limit_denominator()})'
    x2 = f'{Fraction(-b/(2 * a)).limit_denominator()} - i√({Fraction(abs(delta)/(4 * (a ** 2))).limit_denominator()})'
  
  return f'Your roots are complex and they are equal of \nx1 = {x1}\nx2 = {x2}'
