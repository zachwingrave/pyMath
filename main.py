
def power(n, m):
  """ Return base 'n' to power of exponent 'm' """
  if m == 0:
    return 1
  else:
    return n*power(n, m-1)

def percentage_difference_a(n, m):
  """ Return percentage difference of 'n' over 'm' """
  return ((n-m)/m)*100

def percentage_difference_b(n, m):
  """ Return percentage difference of 'n' over 'm' """
  return ((n/m)*100)-100
