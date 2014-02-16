#!/usr/bin/env python
f = open('thirteentext','r')
l=f.readlines()
f.close()
sum = 0
for i in l:
 i=int(i.strip())
 sum += i
print sum
