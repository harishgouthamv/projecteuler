# -*- coding: utf-8 -*-
'''
Problem  - Pandigital prime
Issue - #44
Description -
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
def isprime(num):
  if(num == 1):
    return False
  elif(num == 2):
    return True
  elif(num % 2 == 0):
    return False
  else:
    lim = round(num / 2) + 1
    for x in range(3, lim):
      if(num % x == 0):
        return False
  return True

getpan = lambda n: {x for x in range(1,len(str(n))+1)}
sList= [0] + [sum(getpan(10 ** n)) for n in range(10)]
ispansum = lambda n: sList[len(str(n))] == sum({int(y) for y in str(n)})
ispan = lambda n: getpan(n).symmetric_difference({int(y) for y in str(n)}) == set()


for n in range(111, 987654322, 2):
  if isprime(n) and ispansum(n) and ispan(n):
    print(n)
