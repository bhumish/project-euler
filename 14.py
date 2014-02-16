#!/usr/bin/env python
t=[]
for i in range(1,1000000):
 l=[i]
 s = len(l)
 while not i==1:
  if i%2 == 0:
   i = i/2
   l.append(i)
  else:
   i = 3*i + 1
   l.append(i)
 if s<len(l):
  t = l
print t
