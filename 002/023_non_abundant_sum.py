# -*- coding: utf-8 -*-
'''
Problem  - Non-abundant sums
Issue - #25
Description -
A perfect number is a number for
which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the
proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its
proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number,
1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24.

By mathematical analysis,it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
'''
import math
from itertools import combinations_with_replacement

def get_divisors(num):
    sum = 0
    i = 1
    rt = int(math.sqrt(num))
    while i <= rt:
        if num % i == 0:
            div = int(num / i)
            if div == i or div == num:
                sum += i
            else:
                sum += (i + div)
        i += 1
    return sum

if __name__ == "__main__":
    range_num = {x for x in range(1, 28124)}
    a_num = [x for x in range_num if get_divisors(x) > x]
    a_sum = set(map(lambda x: sum(x), combinations_with_replacement(a_num, 2)))
    print(sum(range_num.difference(a_sum)))
