# -*- coding: utf-8 -*-
'''
Problem  - Circular primes
Issue - #38
Description -
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def rotate(num):
  l = []
  s = c = len(str(num))
  while s != 1:
    s -= 1
    w = (10 ** (c - 1))
    a = int(num / w)
    r = ((num % w) * 10) + a
    num = r
    l.append(r)
  return l

def isprime(num):
  if(num == 2):
    return True
  elif(num % 2 == 0):
    return False
  else:
    lim = round(num / 2) + 1
    for x in range(3, lim):
      if(num % x == 0):
        return False
  return True

c = 0

for num in range(2, 1000001):
  if (isprime(num)):
    for x in rotate(num):
      if not isprime(x):
        break
    else:
      c += 1

print(c)