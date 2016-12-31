
def checkio(n):
  m3 = n % 3 == 0
  m5 = n % 5 == 0
  if m3 and m5:
    return 'Fizz Buzz'
  elif m3:
    return 'Fizz'
  elif m5:
    return 'Buzz'
  else:
    return str(n)
