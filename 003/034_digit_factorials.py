# -*- coding: utf-8 -*-
'''
Problem  - Digit factorials
Issue - #37
Description -
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial

s = 0

c = 10

while True:
  if(sum([factorial(int(x)) for x in str(c)]) == c):
    s += c
    print(s)
  c += 1