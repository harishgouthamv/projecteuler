# -*- coding: utf-8 -*-
'''
Problem  - Truncatable primes
Issue - #40
Description -
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

c = 0
num = 11
csum = 0

while c != 11:
  if isprime(num):
    l = len(str(num))
    s = set()
    left = [num % (10**x) for x in range(1, l+1)]
    right = [int(num / (10**x)) for x in range(l)]
    for n in set(left + right):
      if not isprime(n):
        break
    else:
      c += 1
      csum += num
      print(num)
  num += 1

print(csum)