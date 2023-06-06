import cmath, math
from fractions import Fraction
import AnalyseDiscriminant

class EquationSecondDegree:
  @staticmethod
  def SolveEquation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
     resultado = AnalyseDiscriminant.DiscriminantPositive(coef1, coef2, coef3)
     return resultado
    elif delta == 0: #if there's a discriminant = 0 so x1 = x2
      resultado = AnalyseDiscriminant.DiscriminanteNule(coef1, coef2)
      return resultado
    else:
      resultado = AnalyseDiscriminant.DiscriminantNegative(coef1, coef2, coef3)
      return resultado
    
equationseconddegree = EquationSecondDegree()

coef1, coef2, coef3 = AnalyseDiscriminant.InputABC()

resultado = equationseconddegree.SolveEquation(coef1, coef2, coef3)

if __name__ == "__main__":
  print(resultado)
