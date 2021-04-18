# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
min = 2
max = 21

result = None

count = 2

while result == None:
    for x in range(min, max):
        if(count % x != 0):
            break
    else:
        result = count
    count += 1

print("result= "+ str(result))
