# -*- coding: utf-8 -*-
'''
Problem  - Pandigital products
Issue - #35
Description -
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
'''
from itertools import permutations

pdigits = [str(x) for x in range(1,10)]

pset = set()

for perm in permutations(pdigits, 9):
  pandigit = "".join(perm)
  for x in range(1, 8):
    multiplicand = int(pandigit[:x])
    for y in range(x+1, 9):
      multiplier = int(pandigit[x:y])
      product = int(pandigit[y:])
      if product > multiplicand and product > multiplier and (multiplicand*multiplier == product):
        print(multiplicand, multiplier, product)
        pset.add(product)

print(sum(pset))