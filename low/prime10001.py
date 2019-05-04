# -*- coding: utf-8 -*-
'''
10001st prime #8
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def isprime(num):
    if(num == 2):
        return True
    elif(num % 2 == 0):
        return False
    else:
        lim = round(num / 2) + 1
        for x in range(3, lim):
            if(num % x == 0):
                return False
    return True

count = 0
number = 2
result = None

while count != 10001:
    if(isprime(number)):
        result = number
        count += 1
    number += 1

print("result= " + str(result))
