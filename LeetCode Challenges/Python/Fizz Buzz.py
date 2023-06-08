"""Classic one
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
Source: https://leetcode.com/problems/fizz-buzz/"""

class Solution:
    def fizzBuzz(self, n: int):
        final = []
        for c in range(1, n + 1):
            if c % 3 == 0 and c % 15 == 0: final.append('FizzBuzz')
            elif c % 3 == 0:final.append('Fizz')
            elif c % 5 == 0:final.append('Buzz')
            elif c % 5 != 0 and c % 3 != 0: final.append(str(c))
        return final
