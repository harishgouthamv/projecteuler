# -*- coding: utf-8 -*-
'''
Problem  - Goldbach's other conjecture
Issue - #49
'''
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

x = 9

primes = {2, 3, 5, 7}

while True:
  if not isprime(x):
    for n in range(max(primes)+2, x, 2):
      if isprime(n): primes.add(n)
    for n in primes:
      lhs = int((x - n) / 2)
      m = 1
      rhs = lambda a : a ** 2
      while rhs(m) < lhs: m += 1
      if rhs(m) == lhs: break
    else:
      print(str(x) + " is not gold")
      break
  x += 2