#!/usr/bin/env python
import time
t0 = time.time()
counter = 1
temp = 1
topLimit = 7830457
while counter <= topLimit:
    temp *= 2
    sTemp = str(temp)
    if len(sTemp) > 10:
        temp = int(sTemp[-10:])
    counter += 1
print counter, temp

answer = 28433 * temp + 1
answer = int(str(answer)[-10:])
print answer, "answer"
t1 = time.time()
total = t1 - t0
print total, "seconds"
