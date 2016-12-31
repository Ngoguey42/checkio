
def recall_password(mask, grid):
  from itertools import chain

  def compress(data, selectors):
    return (d for d, s in zip(iter(data), iter(selectors)) if s == 'X')
  def compress2d(data2d, selectors2d):
    m = map(compress, data2d, selectors2d)
    return chain.from_iterable(m)

  pw = []
  for _ in range(4):
    pw = chain(pw, compress2d(grid, mask))
    mask = list(zip(*mask[::-1]))
  return ''.join(pw)


if __name__ == '__main__':
  print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))
