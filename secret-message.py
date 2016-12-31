
def find_message(s):
  return ''.join(filter(lambda x: x.isupper(), s))
  # return ''.join(c for c in s if c.isupper())
  # return ''.join(__import__('re').findall('[A-Z]{1}', s))
