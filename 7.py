#!/usr/bin/env python
import sys
#This is own, working.
def pri(n):
    """Checks if its prime, returns True"""
    if n%2 == 0:
        return ("Not a prime, even number.")
    sqt = int(n**0.5) + 1
    for i in range(3,sqt,2):
        if n%i == 0:
            return ("It is divisible by ",i)
    return True

def genp(t):
  """Generates a list lst of primes till the last number 't' specified with a total of how many primes are generated."""
  lst = [2]
  while len(lst)<t:  
    for i in range(3,104750,2):
        if pri(i) == True:
            lst.append(i)
  print (lst)
  ln = len(lst)
  print ("Total primes till %d is --%d--" %(t,ln))
  sys.exit()

def main():
 i = input("1 to generate list of primes, 2 to check if it is prime\n")
 if i == 1:
  t = input("Enter the last number: ")
  genp(t)
 elif i == 2:
  n = input("Enter the number to check if its prime: ")
  pri(n)
 else:
  print "Enter valid number\n"
  main()


if __name__ == '__main__':
 main()
