#!/usr/bin/env python
def score(name):
 total = 0
 for char in name:
  total += (ord(char)-64)
 return total

def main():
 infile = open('names.txt','r')
 file_contents = infile.read()
 infile.close()
 listofnames = file_contents.split(',')
 listofnames.sort()
 position = 1
 total = 0
 for name in listofnames:
  name = name.strip('"')
  total += score(name)*position
  position+=1
 print total

if __name__ == '__main__':
 main()
