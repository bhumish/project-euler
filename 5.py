#!/usr/bin/env python

lst=[]
for i in range(232792560,232792562):
 if i%16==0 and i%20==0 and i%13==0 and i%17==0 and i%15==0 and i%19==0 and i%18==0 and i%11==0 and i%12==0 and i%14==0:
  lst.append(i)
print lst
