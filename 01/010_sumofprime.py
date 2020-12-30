# -*- coding: utf-8 -*-
'''
Summation of primes - Problem 10 #11

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

max = 2_000_000

def isprime(num):
    lim = round(num / 2) + 1
    for x in range(3, lim):
        if(num % x == 0):
            return False
    return True

result = set()
result.add(2)
for x in range(3, max, 2):
    if isprime(x):
        result.add(x)

print("result= " + str(sum(result)))
