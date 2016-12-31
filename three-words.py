
def checkio(s):
  acc = 0
  for ss in s.split():
    acc = acc + 1 if ss.isalpha() else 0
    if acc == 3:
      return True
  return False
  # import re
  # return bool(re.findall('(\D+\s\D+\s\D+)', s))
