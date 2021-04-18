# -*- coding: utf-8 -*-
'''
Problem  - Consecutive prime sum
Issue - #53
'''
def isprime(num):
  if(num == 1):
    return False
  elif(num == 2):
    return True
  elif(num % 2 == 0):
    return False
  else:
    lim = round(num / 2) + 1
    for x in range(3, lim):
      if(num % x == 0):
        return False
  return True

m = 1000000

primes = [2] + [x for x in range(3, m, 2) if isprime(x)]
#print(primes)
msum = 0
mpl = 0
for x in range(len(primes)-1):
  for y in range(1,len(primes)+1):
    if x != y:
      p = primes[x:y]
      pl = len(p)
      s = sum(p)
      if s < m and pl > mpl and s in primes:
        msum = s
        mpl = pl
        print(s)
      elif s > m:
        break
print(msum)
print(mpl)