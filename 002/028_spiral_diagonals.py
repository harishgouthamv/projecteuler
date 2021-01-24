# -*- coding: utf-8 -*-
'''
Problem  - Number spiral diagonals
Issue - #31
Description -
What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
'''
# Create an array of range 1001**2
# spit array of based in the odd number square minus the previous odd number square.
# The diagonal numbers are the current odd num minus 1.
import numpy as np

n = 1001

arr = np.arange(1, (n**2)+1)

total = 0
preodd = 0

for x in range(1, (n + 1), 2):
    dim = arr[preodd:x**2]
    step = 1 if x == 1 else x - 1
    sub_sq = dim[preodd**2::step]
    total += sum(sub_sq)
    preodd = x
print(total)
