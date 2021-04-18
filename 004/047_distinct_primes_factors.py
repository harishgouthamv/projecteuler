# -*- coding: utf-8 -*-
'''
Problem  - Distinct primes factors
Issue - #50
'''
from functools import reduce

d = []
n = 10000
r = lambda x,y: x * y

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

def prime_factors(x):
  primef = []
  n = 2
  if x % n == 0:
    primef.append(n)
  for i in range(3, int(x / 2) + 1, 2):
    if x % i == 0 and isprime(i):
      primef.append(i)
  return primef

def isprimefactor(n, primef):
  global r
  for x in range(len(primef)):
    d = primef.copy()
    d[x] **= 2
    if reduce(r, d) == n: return True
  return False


while True:
  primef = prime_factors(n)
  #print(n,len(primef))
  if len(primef) == 4 and (reduce(r, primef) == n or isprimefactor(n, primef)):
    if d.count(n-1) != 1: d.clear()
    d.append(n)
  if len(d) == 4: break
  n += 1

print(d)