#!/usr/bin/env python
def triNum(n):
    return sum(range(1,n+1))

def factors(n):
    if (n == 1): return [1]
    a = []
    i = 1
    max = n
    while (i < max):
        if (n % i == 0):
            a.append(i)
            if (i != int(n/i) ): a.append(int(n/i))
            max = int(n/i)
        i += 1   
    return sorted(a)

i=1
while(len(factors(triNum(i))) < 500):
    i += 1

print("answer: ", triNum(i))  
