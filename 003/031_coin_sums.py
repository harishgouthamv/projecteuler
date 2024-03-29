# -*- coding: utf-8 -*-
'''
Problem  - Coin Sums
Issue - #34
Description -
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
target = 201
ways = [0] * target
ways[0] = 1

for x in [1,2,5,10,20,50,100,200]:
  for y in range(x,target):
    ways[y] += ways[y - x]

print(ways[target-1])