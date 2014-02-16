#!/usr/bin/env python
def fact(n):
 if n==0:
  return 1
 else:
  return n*fact(n-1)

def main():
 ls = []
 for i in range(1,100000):
  total = 0
  for j in str(i):
   j = int(j)
   total+=fact(j)
  if total == i:
   ls.append(i)
 print ls

if __name__ == '__main__':
 main()
