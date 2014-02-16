#!/usr/bin/env python
ssq=0
sqs=0
cou=0
for i in range(1,101):
 ssq += (i*i)
 cou += i
sqs = cou*cou
print (sqs-ssq)
