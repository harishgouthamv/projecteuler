# -*- coding: utf-8 -*-
'''
Problem  - Lexicographic permutations
Issue - #26
Description -
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are listed
numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
from itertools import permutations

pset = [x for x in range(0, 10)]
mil_num = ''.join([str(y) for y in ([x for x in permutations(pset, 10)][999_999])])
print(mil_num)