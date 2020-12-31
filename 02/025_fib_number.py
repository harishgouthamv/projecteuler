# -*- coding: utf-8 -*-
'''
Problem  - 1000-digit Fibonacci number
Issue - #27
Description -
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
import math
import numpy as np

phi = np.array((( 1 + math.sqrt(5) ) / 2), dtype=np.longdouble)
div = np.array(math.sqrt(5), dtype=np.longdouble)
nfib = lambda n: int(np.ceil(np.log10(np.divide(np.power(phi,n), div))))
n = 5000
while not nfib(n) < 1000: n -= 1
print(n+1)