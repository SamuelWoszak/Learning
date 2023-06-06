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
              x1 = (-b + math.sqrt(delta))/(2 * a) #show int root 1
              x2 = (-b - math.sqrt(delta))/(2 * a) #show int root 2
          else:
            x1 = f'{(-b + math.sqrt(delta))/(2)}/{a}' #show root in a denominator
            x2 = f'{(-b+ math.sqrt(delta))/2}/{a}' #show root in a denominator
        else:
          if (-b + math.sqrt(delta))/a == 0 and (-b - math.sqrt(delta)) % a == 0: #check if they odd divisible by a
            x1 = f'{(-b + math.sqrt(delta))/a}/2' #show root in 2 denominator
            x2 = f'{(-b - math.sqrt(delta))/a}/2' #show root in 2 denominator
          else:
            x1 = f'{(-b + math.sqrt(delta))}/{2 * a}' #show root in 2a denominator
            x2 = f'{(-b - math.sqrt(delta))/a}/{2 * a}' #show root in 2a denominator
      else:
        x1 = f'({-b} + √{delta})/{2 * a}' #show root in 2a denominator and not exact root
        x2 = f'({-b}) - √{delta}/{2 * a}' #show root in 2a denominator and not exact root
      print(f'The roots are real and they are {x1} and {x2}!') #show roots
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
      print(f'Your roots have multiplicity and they are equal {x1}!') #return the value of the "root" (its two roots, i know, they r just the same.)
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
      print(f'Your roots are complex and they are {x1} and {x2}!')
equationseconddegree = EquationSecondDegree()
equationseconddegree.SolveEquation(a, b, c)
