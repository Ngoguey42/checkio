
def checkio(i):
  from functools import reduce
  from operator import mul
  return reduce(mul, (int(x) for x in str(i) if x != '0'))

  # res = 1
  # for d in str(i):
    # res *= int(d) if d != '0' else 1
  # return res
