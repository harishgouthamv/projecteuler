# -*- coding: utf-8 -*-
'''
Problem  - Amicable numbers
Issue - #23
Description -
Let d(n) be defined as the sum of proper divisors of
n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors
of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math


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


def amicable_numbers(num):
    a_num = set()
    for i in range(0, num):
        r0 = get_divisors(i)
        r1 = get_divisors(r0)
        if i != r0 and r1 == i:
            a_num.add(i)
            a_num.add(r0)
    return sum(a_num)


if __name__ == "__main__":
    print(amicable_numbers(10000))
