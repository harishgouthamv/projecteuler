# -*- coding: utf-8 -*-
'''
Problem  - Pandigital multiples
Issue - #41
Description -
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
p9digit = 0
dig9 = {str(x) for x in range(1,10)}
n = 1
while True:
  oldres = None
  res = None
  m = 1
  while res is None or int(res) <= 987654321:
    if res is None: res = str()
    oldres = str(res)
    res += str(n * m)
    m += 1
  if (len(oldres) == 9) and not {y for y in oldres}.symmetric_difference(dig9) and int(oldres) > p9digit:
    p9digit = int(oldres)
    print(p9digit)
  n += 1
