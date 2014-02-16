#!/usr/bin/env python
def rev(n,pt = 0):
 if n==0:
  return pt
 return	rev(n/10,pt*10+n%10)

i = []
for t in range(900,1000):
 for s in range(900,1000):
  pro = s*t
  if rev(pro) == pro:
   i.append(pro)
print i

