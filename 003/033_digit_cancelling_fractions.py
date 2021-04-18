# -*- coding: utf-8 -*-
'''
Problem  - Digit cancelling fractions
Issue - #36
Description -
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''
from math import gcd
dprod = 1
nprod = 1

for i in range(1, 10):
  for n in range(1, 10):
    for d in range(1, 10):
      if ((n * 10 + i) * d) == (n * (i * 10 + d)):
        dprod *= d
        nprod *= n

print(dprod/gcd(nprod, dprod))