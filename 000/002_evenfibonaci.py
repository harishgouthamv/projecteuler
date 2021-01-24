'''
Find sum of the even fibonaci numbers less than 4 million.
'''
upper_limit = 4000000
fiblist = [1,2]
while fiblist[-1] < upper_limit: fiblist += [fiblist[-1] + fiblist[-2]]
evensum = sum([x for x in fiblist if x % 2 == 0])
print(evensum)
