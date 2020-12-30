# -*- coding: utf-8 -*-
'''
Special Pythagorean triplet #10

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import itertools

min = 1
max = 1000
result = None
val = [x for x in range(min, max)]

for e in itertools.product(val, val, val):
    a = e[0]
    b = e[1]
    c = e[2]
    if (a < b) and (b < c) and(((a ** 2) + (b ** 2)) == (c ** 2)) and (a + b + c == 1000):
        result = a * b * c
        break
print("result= " + str(result))
