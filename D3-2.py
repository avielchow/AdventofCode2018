import sys
import re
import numpy as np
sys.stdin = open('Input.txt','r')
inputlist = []
dimensions = []


matrix = np.zeros((1220,1220))

for x in map(str.rstrip,sys.stdin):
  inputlist.append(x)

for x in inputlist:
  findnumber = re.compile(r"\d*")
  newinputlist = findnumber.findall(x)
  newinputlist = list(filter(lambda a: a != "", newinputlist))
  dimensions.append(newinputlist[0:5])


def addtomatrix(horizontal,vertical,width,length):
  matrix[vertical:length, horizontal:width] += 1


for x in dimensions:
  x = [int(a) for a in x]
  x[3] = x[1] + x[3]
  x[4] = x[2] + x[4]
  addtomatrix(x[1], x[2], x[3], x[4])


for x in dimensions:
  x = [int(a) for a in x]
  x[3] = x[1] + x[3]
  x[4] = x[2] + x[4]
  check = (matrix[x[2]:x[4],x[1]:x[3]])
  if np.all(check == 1) == True:
    print (x[0])



#1 @ 4,6: 1x3



