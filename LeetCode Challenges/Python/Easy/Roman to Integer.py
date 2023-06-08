#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
    def romanToInt(self, s: str) -> int:
          informations = {
                      'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C':100,
                      'D':500,
                      'M':1000
                  }
          finalNumber = 0
          hold = 0
          for c in reversed(s.upper()):
            number = informations.get(c)
            if hold != 0:
              if number >= hold:
                finalNumber += number
              else:
                finalNumber -= number
            else:
              finalNumber += number
            hold = number
          return finalNumber
