import chronos

# hello world
print(chronos.test())

# test timer function
def fib_lin(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

def fib_exp(n):
  if n <= 1:
    return n
  return fib_exp(n-1) + fib_exp(n-2)

def fib_const(n):
  dp = {i:fib_lin(i) for i in range(100)}
  return dp[n]

print("running linear time function")
func, coeff = chronos.timer(fib_lin, silent=True, num=100)
print(func, coeff, "\n")

print("running constant time function")
func, coeff = chronos.timer(fib_const, silent=True, num=50)
print(func, coeff)
