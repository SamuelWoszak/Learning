#You need to calculate the int part of a sqrt(x) but you CANT use ANY POWER PROPERTY or MULTIPLICATION envolving x (the number that YOU are using).
class Solution:
    def mySqrt(self, x: int) -> int:
        soma, n = 0, 0
        while soma < x:
            soma += 2 * n + 1
            n += 1
        if n != 0:
            if soma == x:
                return int(soma/n)
            else:
                return int((soma-1)/n)
        else:
            return 0
          
#Explain: an perfect square can be write as the sum of the first n digits by n², u can proof this by using de P.A formula with n = 1 and ending at n, the number
#that you want to know the square root.
#By the first comment, you can see that the only time that i use "x" is in the if and the while, you cant use math.sqrt(x) or pow() or ** function, and not envolve x
#anywhere
