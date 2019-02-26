import sys
from collections import Counter
sys.stdin = open('Input.txt','r')
inputlist = []
for x in map(str.rstrip,sys.stdin):
  inputlist.append(x)  

def check(first,second):
  count = 0
  for x in range(len(first)):
    if first[x] != second[x]:
      count = count + 1
  if count == 1:
    print (first)
    print (second)


for x in inputlist:
  for y in inputlist:
    if x != y:
      check(x,y)
      
