# -*- coding: utf-8 -*-
'''
Problem  - Quadratic primes
Issue - #30
Description -
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with n=0.
'''
def isprime(n):
    num = abs(n)
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

if __name__ == "__main__":
    max_n = 0
    max_prod = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1001):
            n = 0
            while isprime((n * n) + (a * n) + (b)): n += 1
            n -= 1
            if n > max_n:
                max_n = n
                max_prod = a * b
    print(max_prod)
