# -*- coding: utf-8 -*-
'''
Problem  - Sub-string divisibility
Issue - #46
'''
pan = {x for x in range(10)}
pansum = lambda n: sum({int(y) for y in str(n)}) == 45
ispan = lambda n: pan.symmetric_difference({int(y) for y in str(n)}) == set()

s = 0

for x in range(1000000000,9999999999):
#def test(x):
#  global s
  if pansum(x) and ispan(x):
    y = str(x)
    min,max = (1,4)
    primes = [17, 13, 11, 7, 5, 3, 2]
    while max <= 10:
      if (int(y[min:max]) % primes.pop()) != 0:
        break
      min += 1
      max += 1
    else:
      s += x
      print(x)
      print(s)

#test(1406357289)
print(s)