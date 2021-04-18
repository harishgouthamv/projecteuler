# -*- coding: utf-8 -*-
'''
Problem  - Coded triangle numbers
Issue - #45
'''
import string
import numpy as np

data = np.loadtxt('artefacts/p042_words.txt', dtype=str, delimiter=',')
alpha_dict = {v:k+1 for k,v in enumerate(string.ascii_uppercase)}
tri_num = [int((n * (n + 1)) / 2) for n in range(1, 27)]
is_tri_num = lambda x: sum([alpha_dict[y] for y in x]) in tri_num
print(len(list(filter(is_tri_num, data))))