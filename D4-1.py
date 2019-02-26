
import sys
import re
from functools import reduce
import numpy as np
from operator import itemgetter

newinputlist = []

sys.stdin = open('Input.txt','r')
for x in sys.stdin:
  splitter = re.compile(r"\d+")
  inputlist = splitter.findall(x)
  inputlist = [int(x) for x in inputlist]
  if inputlist[3] == 23:
    inputlist[4] = 0
    newinputlist.append(inputlist)
  else:
    newinputlist.append(inputlist)

newinputlist.sort()
timeasleep = {}

for x in newinputlist:
  if len(x) == 6:
    keyholder = x[5]
    if x[5] not in timeasleep:
      timeasleep[x[5]] = []
  if len(x) < 6:
    timeasleep[keyholder].append(x[4])

'''returns guard #, Totaltimeasleep, Minutemostasleep'''

def evaluateguard(x):
  guard = timeasleep[x]
  matrix = np.zeros((1,60))
  totaltimeasleep = 0
  for y in range(len(guard)):
    if y%2==0:
      lowerlimit = guard[y]
      upperlimit = guard[y+1]
      matrix[:, lowerlimit:upperlimit] += 1
      totaltimeasleep += (upperlimit-lowerlimit)
  matrix = list(max(matrix))
  Frequencyminute = max(matrix)
  Minute = matrix.index(Frequencyminute)
  return x, totaltimeasleep, Minute

''' List of all Guard Data'''
guarddata=[]
for key in timeasleep:
  guarddata.append(evaluateguard(key))

'''Final Results'''

Guardmostasleep = (max(guarddata, key=itemgetter(1))[0])
Minutemostasleep = (max(guarddata, key=itemgetter(1))[2])
print (max(guarddata, key=itemgetter(1)))
print (Guardmostasleep)
print (Minutemostasleep)

