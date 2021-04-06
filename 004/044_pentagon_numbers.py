# -*- coding: utf-8 -*-
'''
Problem  - Pentagon numbers
Issue - #47
'''
from math import sqrt

def isPentagonal(n):
  p = (sqrt(1.0 + (24.0 * n)) + 1.0) / 6.0
  return p == int(p)

p = lambda n: n * (3 * n - 1) / 2
result = 0
i = 0

while True:
  i += 1
  n = p(i)
  for j in reversed(range(1, i)):
    m = p(j)
    if isPentagonal(n - m) and isPentagonal(n + m):
      result = n - m
      break
  else:
    continue
  break

print(result)