# -*- coding: utf-8 -*-
'''
Problem  - Names scores
Issue - #24
Description -
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import string
import numpy as np

from functools import reduce

alpha_dict = {v:k+1 for k,v in enumerate(string.ascii_uppercase)}

data = np.loadtxt('artefacts/p022_names.txt', dtype=str, delimiter=',')
sdata = np.sort(data)

vdata = list(map(lambda x: sum([alpha_dict[y] for y in x]), sdata))
ndata = sum([((i + 1) * v) for i,v in enumerate(vdata)])
print(ndata)
