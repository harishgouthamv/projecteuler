# -*- coding: utf-8 -*-
'''
Problem  - Champernowne's constant
Issue - #43
Description -
https://projecteuler.net/problem=40
'''
n = 1
s = str(0)
m = 1
while len(s) <= 1000001:
  s += str(n)
  n+=1
darr = [int(d) for d in s]
p = darr[1] * darr[10] * darr[100] * darr[1000] * darr[10000] * darr[100000] * darr[1000000]
print(p)