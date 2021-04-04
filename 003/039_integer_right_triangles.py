# -*- coding: utf-8 -*-
'''
Problem  - Integer right triangles
Issue - #42
Description -
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
from itertools import combinations_with_replacement, permutations

py = lambda x : ((x[0] ** 2) + (x[1] ** 2)) == (x[2] ** 2)

l = 0

for x in range(3, 1001):
  s = set()
  #s |= {p for p in permutations(range(1, x+1), 3) if sum(p) == x }
  s |= {p for p in combinations_with_replacement(range(1, x+1), 3) if sum(p) == x }
  plist = [list(p) for p in s if py(p)]
  nl = len(plist)
  if nl > l:
    l = nl
    print(l)
    print(plist)
    print(x)
