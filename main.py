from string import ascii_letters
from string import digits
from string import punctuation
import itertools

ALPHABET = digits + ascii_letters + punctuation

def power(n, m):
  ''' Return base 'n' to power of exponent 'm' '''
  if m == 0:
    return 1
  else:
    return n * power(n, m - 1)

def base_string(b):
  ''' Return digits of base 'b' as a string. '''
  return ALPHABET[:b]

def absolute_value(n, b):
  ''' Return absolute value of 'n' where 'n' is base 'b'. '''
  n_digits = str(n)
  b_digits = base_string(b)
  current_power = b - 1
  value = 0

  for digit in n_digits:
    n_digit_val = b_digits.find(digit)
    value += n_digit_val * power(b, current_power)
    current_power -= 1

  return value

def percentage_difference_a(n, m):
  ''' Return percentage difference of 'n' over 'm' '''
  return ((n/m)*100)-100

def percentage_difference_b(n, m):
  ''' Return percentage difference of 'n' over 'm' '''
  return ((n-m)/m)*100

if __name__ == '__main__':
  pass
