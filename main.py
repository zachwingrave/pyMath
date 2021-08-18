from string import ascii_letters
from string import digits
from string import punctuation
import itertools

ALPHABET = ascii_letters + digits + punctuation

def power(n, m):
  """ Return base 'n' to power of exponent 'm' """
  if m == 0:
    return 1
  else:
    return n*power(n, m-1)

def find_position(word, alphabet=ALPHABET):
  current_power = len(word) - 1
  base = len(ALPHABET)
  pos = 0
  for char in word:
    char_pos = alphabet.find(char) + 1
    pos += char_pos * power(base, current_power)
    current_power -= 1
  return pos

def test_find_pos(word, alphabet=ALPHABET):
  counter = 1
  for length in range(1, len(word) + 1):
    wordlist = itertools.product(alphabet, repeat=length)
    for word in wordlist:
      if find_position(word) != counter:
        print('Error at position', counter)
        return False
      counter += 1
  return True

def percentage_difference_a(n, m):
  """ Return percentage difference of 'n' over 'm' """
  return ((n/m)*100)-100

def percentage_difference_b(n, m):
  """ Return percentage difference of 'n' over 'm' """
  return ((n-m)/m)*100
