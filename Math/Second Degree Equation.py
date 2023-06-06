#this code shows when isnt a exact root, complex or real roots, frac result also int results
import cmath, math

class EquationSecondDegree:
  @staticmethod
  def SolveEquation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
      if math.sqrt(delta) == int(math.sqrt(delta)):
        if (-b + math.sqrt(delta)) % 2 == 0: #simplify by 2
          if ((-b + math.sqrt(delta))//2) % a == 0 and ((-b - math.sqrt(delta))// 2) % a == 0: #simplify by a because they r multiply 
              x1 = (-b + math.sqrt(delta))/(2 * a)
              x2 = (-b - math.sqrt(delta))/(2 * a) 
          else:
            x1 = f'{(-b + math.sqrt(delta))/(2)}/{a}'
            x2 = f'{(-b+ math.sqrt(delta))/2}/{a}'
        else:
          if (-b + math.sqrt(delta))/a == 0 and (-b - math.sqrt(delta)) % a == 0:
            x1 = f'{(-b + math.sqrt(delta))/a}/2'
            x2 = f'{(-b - math.sqrt(delta))/a}/2'
          else:
            x1 = f'{(-b + math.sqrt(delta))}/{2 * a}'
            x2 = f'{(-b - math.sqrt(delta))/a}/{2 * a}'
      else:
        x1 = f'({-b} + √{delta})/{2 * a}'
        x2 = f'({-b}) - √{delta}/{2 * a}'
      print(f'As raízes são {x1} e {x2}!')
    elif delta == 0: #if there's a discriminant = 0 so x1 = x2
      if b % 2 == 0: #if b is pair simplify the frac
        if (b // 2) % a == 0: #if b is multiply of a so simplify
          x1 = -b/(2 * a)
        else: #if its not multiply of a so stay in frac mode
          x1 = f'{-b/2}/{a}'
      else:
          if (b % 2) % a == 0: #if its not pair
            x1 = f'{-b/a}/2' #simplify b with a and stay b/2 bc b/2 isnt int
          else:
            x1 = f'{-b}/{2 * a}' #if b isnt multiply of a and 2 in same time so stay in frac mode
      print(f'Sua raíz é de multiplicidade dois e ambas valem {x1}!') #return the value of the "root" (its two roots, i know, they r just the same.)
        #done
    else:
      z = complex(b, delta)
      if z.real % 2 == 0 and z.imag % 4 == 0: #check if both are pair to simplify the frac
        if ((z.real // 2) % a) == 0 and ((z.imag // 4) % (a ** 2)) == 0: #check if both are multiply of "a" to simplify the frac (it was simplfied early)
          if math.sqrt(abs(delta)) == int(math.sqrt(abs(delta))): #see if the root is exactly to simplify
            x1 = f'{-z.real/(2 * a)} + i{math.sqrt(abs(z.imag))/(4 * (a ** 2))}'#complex notation
            x2 = f'{-z.real/(2 * a)} - i{math.sqrt(abs(z.imag))/(4 * (a ** 2))}'#complex notation
            print(f'1')
          else:
            x1 = f'{-z.real/(2 * a)} + i√{(abs(z.imag))/(4 * (a ** 2))}' #complex notation with sqrt() symbol bc discriminant isnt exact
            x2 = f'{-z.real/(2 * a)} - i√{(abs(z.imag))/(4 * (a ** 2))}' #complex notation with sqrt() symbol bc discriminant isnt exact   
            print(f'2 {math.sqrt(abs(delta))}, {int(math.sqrt(abs(delta)))}, {(z.imag)}')
        else:
          if math.sqrt(abs(delta)) == int(math.sqrt(abs(delta))): #see if the root is exactly to simplify
            x1 = f'({-z.real/(2)} + i{math.sqrt(abs(z.imag))/(4)})/{a}'#complex notation
            x2 = f'({-z.real/(2)} - i{math.sqrt(abs(z.imag))/(4)})/{a}'#complex notation
            print('3')
          else:
            x1 = f'({-z.real/(2)} + i√{(abs(z.imag))/(4)})/{a}'#complex notation
            x2 = f'({-z.real/(2)} - i√{(abs(z.imag))/(4)})/{a}'#complex notation
            print('4')
          
      if z.real % 2 != 0 or z.imag % 4 != 0: #odd a and b (saying a + bi form)
        if z.real % a == 0 and z.imag % (a ** 2) == 0: #if they r multiply of a
          if math.sqrt(abs(delta)) == int(math.sqrt(abs(delta))):  #if exact discriminant
            x1 = f'(-{z.real/a} + i{math.sqrt(abs(z.imag))/(a ** 2)})/2' #print root simplified by a
            x2 = f'(-{z.real/a} - i{math.sqrt(abs(z.imag))/(a ** 2)})/2' #print root simplified by a
            print('5')
          else:
            x1 = f'(-{z.real/a} + i√{(abs(z.imag))/(a ** 2)})/2' #print root simplified by a but discriminant isnt exact
            x2 = f'(-{z.real/a} - i√{(abs(z.imag))/(a ** 2)})/2' #print root simplified by a but discriminant isnt exact     
            print('6')       
        else:
          if math.sqrt(abs(delta)) == int(math.sqrt(abs(delta))):
            x1 = f'(-{z.real} + i{math.sqrt(abs(z.imag))})/{2 * a}' #they are not  divisible by a and 2 and exact root
            x2 = f'(-{z.real} - i{math.sqrt(abs(z.imag))})/{2 * a}' #they are not  divisible by a and 2 and exact root
            print('7')
      print(f'As suas raízes são {x1} e {x2}!')
equationseconddegree = EquationSecondDegree()
equationseconddegree.SolveEquation(3, 4, 2)
