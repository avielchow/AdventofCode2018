import sys
from collections import Counter
sys.stdin = open('Input.txt','r')
inputlist = []
count2 = 0
count3 = 0
switch = True

for x in map(str.rstrip,sys.stdin):
  inputlist.append(x)


for x in inputlist:
  switch = True
  counter = Counter(x)
  for y in x:
    if counter[y] == 3:
      while switch == True:
        count3 = count3 + 1
        switch = False


      
for x in inputlist:
  switch = True
  counter = Counter(x)
  for y in x:
    if counter[y] == 2:
      while switch == True:
        count2 = count2 + 1
        switch = False

print (count2*count3)
  












