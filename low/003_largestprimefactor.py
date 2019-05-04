'''
Largest prime factor #4

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
v = 600851475143

def findNextPrime(num):
    while num < v:
        num += 1
        if(num == 2):
            return num
        elif(num % 2 == 0):
            continue
        else:
            li = round(num / 2) + 1
            for x in range(2, li):
                if(num % x == 0):
                    break
            else:
                return num

f = v
x = set()
count = 1
while f != 1:
    prime = findNextPrime(count)
    if(f % prime == 0):
        f = f / prime
        x.add(prime)
    else:
        count += 1
print(x)
# [5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639]
