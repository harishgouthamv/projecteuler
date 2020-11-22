# -*- coding: utf-8 -*-
'''
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import itertools

max = 1000
min = 100

r3list = [x for x in range(min,max)]

result = 0

for prd in itertools.product(r3list,r3list):
    e = prd[0] * prd[1]
    s1 = str(e)
    if(s1 == s1[::-1]) and result < e:
        result = e

print(result)
