# -*- coding: utf-8 -*-
'''
Problem 20 -
Issue - #21
Description -
Find the sum of the digits in the number 100!
'''
import math

print(sum([int(x) for x in str(math.factorial(100))]))
