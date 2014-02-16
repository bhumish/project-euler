#!/usr/bin/env python
powers = []
grandtotal = 0

for i in range(2,254294):
 total=0
 for j in str(i):
  total += int(j)**5
 if total == i:
  powers.append(i)
for i in powers:
 grandtotal += i

print("powers:",powers)
print("total:",grandtotal)
