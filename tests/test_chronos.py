import chronos

def fib_vannila(n):
    if n <= 1:
        return n
    return fib_vannila(n-1) + fib_vannila(n-2)

def fib_dp(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def fib_linear(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def fib_fast(n):
  lookup = {}
  a, b = 0, 1
  for i in range(50):
      a, b = b, a+b
      lookup[i] = a
  return lookup[n]


def test_fib_vannila():
    assert chronos.timer(fib_vannila) == "$x^2$"