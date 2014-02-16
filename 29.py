#!/usr/bin/env python
ls = []
for a in range(2,101):
 for b in range(2,101):
  s = a**b
  if s not in ls:
   ls.append(s)
print ls
print len(ls)
