# -*- coding: utf-8 -*-
'''
Problem  - Double-base palindromes
Issue - #39
Description -
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''
s = 0
for x in range(1,1000001):
  y = [y for y in str(x)]
  y.reverse()
  if(int("".join(y)) == x):
    #print("acc: " + str(x))
    ba = bin(x).replace("0b", "")
    na = int(ba)
    m = [m for m in str(ba)]
    m.reverse()
    rna = int("".join(m))
    if(na == rna):
      s += x

print(s)