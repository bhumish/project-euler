#!/usr/bin/env python
for i in range(1,1000,1):
 for j in range(1,1000-i,1):
  k = 1000-i-j
  if i**2+j**2 == k**2:
   print i*j*k

