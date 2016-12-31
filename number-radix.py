
def checkio(s, b):
 try:
   return int(s, b)
 except ValueError:
   return -1
