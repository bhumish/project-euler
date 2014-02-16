#!/usr/bin/env python
from itertools import product
 
print max(map(lambda x: sum(map(int,str(x[0]**x[1]))), product(range(1,100),range(1,100))))

