from math import log
from tqdm import tqdm
import numpy as np
import types, time

# lookup table for the trajectories and their derivatives
FXS = {
  "$1$": lambda x: 1,
  "$x$": lambda x: x,
  "$x^2$": lambda x: x**2,
  "$x^3$": lambda x: x**3,
  "$log(x)$": lambda x: np.log(x),
  "$xlog(x)$": lambda x: x*np.log(x),
  "$2^x$": lambda x: 2**x
}

# num of iterations before we can potentially stop early
EARLY_STOP = 20

# main timer function 
def timer(func: types.FunctionType) -> str:
  # init variables for storage
  x = list(range(1, 50))
  y = []
  # time the function
  for i in tqdm(x):
    start = time.time()
    func(i)
    end = time.time()
    y.append(end-start)
  loss, coeffs = [], []

  # run regression for every trajectory
  for func in FXS.values():
    # find best fit via least squares
    coeff = np.linalg.lstsq(np.array([func(i) for i in x]).reshape(-1, 1), y, rcond=None)[0]
    coeffs.append(coeff)
    # find total loss
    loss = np.sum(np.abs(y - coeff*func(x)))
    loss.append(loss)

  # find the best fit
  best = np.argmin(loss)
  # return name of best fit and its coefficient
  return best, coeffs[best]


# empty function for testing functionality
def test():
  return "Hello World"