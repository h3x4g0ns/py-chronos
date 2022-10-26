import chronos

# hello world
print(chronos.test())

# test timer function
def fib_linear(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

def fib_vannila(n):
  if n <= 1:
    return n
  return fib_vannila(n-1) + fib_vannila(n-2)

# print(chronos.timer(fib_linear))
print(chronos.timer(fib_vannila))