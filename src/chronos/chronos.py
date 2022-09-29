from math import log
import types, time

# lookup table for the trajectories and their derivatives
FXS = {
  "$x$": (lambda x: x, lambda x: 1, lambda x: 0),
  "$x^2$": (lambda x: x**2, lambda x: 2*x, lambda x: 2),
  "$x^3$": (lambda x: x**3, lambda x: 3*x**2, lambda x: 6*x),
  "$log(x)$": (lambda x: log(x), lambda x: 1/x, lambda x: -1/x**2),
  "$xlog(x)$": (lambda x: x*log(x), lambda x: log(x) + 1, lambda x: 1/x),
  "$2^x$": (lambda x: 2**x, lambda x: log(2)*2**x, lambda x: log(2)**2*2**x)
}

# num of iterations before we can potentially stop early
EARLY_STOP = 5


# return 2nd degree taylor expansion of f(x) at x0
def taylor_expansion(x0, y, f1, f2):
  return lambda x: y + f1(x0)*(x-x0) + f2(x0)*(x-x0)**2/2


# main timer function 
def timer(func: types.FunctionType) -> str:
  # init variables for storage
  x = list(range(1, 50))
  y = []
  loss = {k: [0] for k in FXS.keys()}
  arg_min = []

  for i in x:
    # record new measure for runtime
    start = time.time()
    func(i)
    elapsed = time.time() - start
    y.append(elapsed)

    # no need to calculate loss for the first iteration
    if i == 1:
      continue
    else:
      for k, v in FXS.items():
        # calculate taylor expansion at given point
        f = taylor_expansion(i, y[i-1], v[1], v[2])
        yhat = f(i)
        # calculate loss for the current iteration
        # and add it to runing sum
        loss[k].append(abs(y[-1] - yhat) + loss[k][-1])

      # caculate argmin for the current iteration
      arg_min.append(min(loss.keys(), key=lambda x: loss[x][-1]))

    # no need to stop early if less than EARLY_STOP iterations
    if len(arg_min) < EARLY_STOP:
      continue
    else:
      # check if the last EARLY_STOP iterations have the same argmin
      if all([arg_min[-1] == arg_min[-i] for i in range(1, EARLY_STOP)]):
        return arg_min[-1]

  # if we get here, we have to return the argmin of the last iteration
  return arg_min[-1]


# empty function for testing functionality
def test():
  return "Hello World"