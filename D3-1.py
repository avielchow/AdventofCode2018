import sys
import re
import numpy as np
sys.stdin = open('Input.txt','r')
inputlist = []
dimensions = []

matrix = np.zeros((1200,1200))

for x in map(str.rstrip,sys.stdin):
  inputlist.append(x)

for x in inputlist:
  findnumber = re.compile(r"\d*")
  newinputlist = findnumber.findall(x)
  newinputlist = list(filter(lambda a: a != "", newinputlist))
  dimensions.append(newinputlist[1:5])


def addtomatrix(horizontal,vertical,width,length):
  matrix[vertical:length, horizontal:width] += 1


for x in dimensions:
  x = [int(a) for a in x]
  x[2] = x[0] + x[2]
  x[3] = x[1] + x[3]
  addtomatrix(x[0], x[1], x[2], x[3])

count = 0

for x in matrix:
  for a in x:
    if a > 1:
      count = count + 1

print(count)



