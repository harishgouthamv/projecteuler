# -*- coding: utf-8 -*-
'''
Problem 17 - Number letter counts
Issue - #18
Description -
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE:
Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

unique_num_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",
    100: "hundred",
    1000: "onethousand"
}

num_letter = str()

def calcTenValue(x):
    num = int(x / 10) * 10
    div = x % 10
    if div == 0:
        return unique_num_dict[num]
    else:
        return unique_num_dict[num] + unique_num_dict[div]

for x in range(1, 1001):
    if len(num_letter) > 10: print(num_letter[-30:])
    if x in unique_num_dict.keys() and x != 100:
        num_letter += unique_num_dict[x]
    elif x > 20 and x < 100:
        num_letter += calcTenValue(x)
    else:
        hnum = int(x / 100)
        hvalue= unique_num_dict[hnum] + unique_num_dict[100]
        tnum = x % (hnum * 100)
        if tnum == 0:
            num_letter += hvalue
        elif tnum < 20:
            num_letter +=  (hvalue + "and" + unique_num_dict[tnum])
        else:
            num_letter += (hvalue + "and" + calcTenValue(tnum))

print(len(num_letter))
