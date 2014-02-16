#!/usr/bin/env python

import math
def squares(row,col):
 return row* (row+1) * col * (col+1) / 4

topl = 2000000
dist = 2000000

for r in range(1,100):
 for c in range(1,100):
  temp = squares(r,c)
  d = int(math.fabs(topl-temp))
  if d<dist:
   answer = (r,c)
   dist = d
print dist, answer
print "area", answer[0]*answer[1]
