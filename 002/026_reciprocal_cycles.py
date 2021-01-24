# -*- coding: utf-8 -*-
'''
Problem  - Reciprocal cycles
Issue - #29
Description -
Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
'''
# Perform division till you get the remainder 1. if it is zero, terminate as it is non
# recurring. What is posibility it is infinite? -> expect recursion error.
import math

def get_div(num, den, m=None):
    flag = False
    while num < den:
        num *= 10
        if m and flag:
            m.append(0,0)
        flag = True
    return num

def find_quotient(num, den, m):
    ret = (True, 0, 0)
    div = get_div(num, den)
    quo = math.floor(div / den)
    rem = div % den
    if (quo, rem) in m:
        ret = (False, quo, rem)
        m.append((quo, rem))
    elif rem == 0:
        m.append((quo, rem))
        ret = (True, 0, 0)
    else:
        m.append((quo, rem))
        ret = find_quotient(rem, den, m)
    return ret

if __name__ == "__main__":
    max_d = 0
    max_count = 0
    for d in range(2, 1000):
        m = list()
        div = get_div(1,d,m)
        is_not_rec, quo, rem = find_quotient(div, d, m)
        if is_not_rec: continue
        i = m.index((quo, rem))
        min_arr = m[i+1:]
        ilen = len(min_arr)
        if ilen > max_count:
            max_d = d
            max_count = ilen
    print(max_d)
