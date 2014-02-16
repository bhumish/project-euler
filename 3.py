#!/usr/bin/env python
from math import sqrt
lst = []
for i in range(1,int(sqrt(600851475143))):
 if 600851475143%i==0:
  lst.append(i)
print lst
prinot = []
for k in lst:
 sq = int(sqrt(k))+1
 for i in range(3,sq,2):
  if k %i == 0:
   prinot.append(k)
print prinot
pri = []
for j in lst:
 if j not in prinot:
  pri.append(j)
print pri
