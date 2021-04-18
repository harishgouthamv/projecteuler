# -*- coding: utf-8 -*-
'''
Problem  - Triangular, pentagonal, and hexagonal
Issue - #48
'''
from math import sqrt

def istri(n):
  x = (sqrt((8 * n) + 1) - 1) / 2
  return x == int(x)

def isPen(n):
  p = (sqrt(1.0 + (24.0 * n)) + 1.0) / 6.0
  return p == int(p)

def isHex(n):
  x = (sqrt((8 * n) + 1) + 1) / 4
  return x == int(x)

c = 40756
while True:
  if istri(c) and isPen(c) and isHex(c):
    print(c)
    break
  c += 1