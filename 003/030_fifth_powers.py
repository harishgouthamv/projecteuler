# -*- coding: utf-8 -*-
'''
Problem  - Digit fifth powers
Issue - #33
Description -
Find the sum of all the numbers
that can be written as the sum of fifth powers of their digits.
'''
i = 2
s = 0
while True:
    y = sum([int(x) ** 5 for x in str(i)])
    if y == i:
        print(y)
        s += y
        print(s)
    i += 1