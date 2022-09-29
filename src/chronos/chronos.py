import numpy as np
from math import log
import types

# lookup table for the trajectories and their derivatives
FXS = {
  "$x$": (lambda x: x, lambda x: 1, lambda x: 0),
  "$x^2$": (lambda x: x**2, lambda x: 2*x, lambda x: 2),
  "$x^3$": (lambda x: x**3, lambda x: 3*x**2, lambda x: 6*x),
  "$log(x)$": (lambda x: log(x), lambda x: 1/x, lambda x: -1/x**2),
  "$xlog(x)$": (lambda x: x*log(x), lambda x: log(x) + 1, lambda x: 1/x),
  "$2^x$": (lambda x: 2**x, lambda x: log(2)*2**x, lambda x: log(2)**2*2**x)
}


# return 2nd degree taylor expansion of f(x) at x0
def taylor_expansion(x0, y, f1, f2):
  return lambda x: y + f1(x0)*(x-x0) + f2(x0)*(x-x0)**2/2

# main timer function 
def timer(func: types.FunctionType, mode: str, inp) -> str:
  pass


# empty function for testing functionality
def test():
  return "Hello World"