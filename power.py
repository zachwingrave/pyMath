
def power(n, m):
  """ Return base 'n' to power of exponent 'm' """
  if m == 0:
    return 1
  else:
    return n*power(n, m-1)
