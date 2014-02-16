#!/usr/bin/env python
import sys
a = 1
b = 2
sum = 0
count = 3
while True:
 sum = a + b
 a = b
 b = sum
 count += 1
 if len(str(sum))==1000:
  print sum
  print count
  sys.exit()
 
