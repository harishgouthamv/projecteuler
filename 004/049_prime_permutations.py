# -*- coding: utf-8 -*-
'''
Problem  - Prime permutations
Issue - #52
'''
from itertools import permutations,combinations

gset = set()

def isprime(num):
  if(num == 1):
    return False
  elif(num == 2):
    return True
  elif(num % 2 == 0):
    return False
  else:
    lim = round(num / 2) + 1
    for x in range(3, lim):
      if(num % x == 0):
        return False
  return True

def find_prime_per(x):
  global gset
  i = {int("".join(m)) for m in permutations([y for y in str(x)])}
  j = {m for m in i if len(str(m)) == 4 and m not in gset and isprime(m)}
  if len(j) >=3:
    for n in combinations(j, 3):
      m = list(n)
      m.sort()
      if (m[1] - m[0]) == (m[2] - m[1]):
        gset |= set(n)
        print(n)

for x in range(1000,10001):
  if x not in gset and isprime(x):
    find_prime_per(x)