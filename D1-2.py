import sys
sys.stdin = open('Input.txt','r')

currentfrequency=0
inputlist=[]
steps=[]
total=set([])
switch = 0

for x in sys.stdin:
  inputlist.append(int(x))

while switch == 0:
  for x in inputlist:
    currentfrequency = x + currentfrequency
    if currentfrequency not in total:
      total.add(currentfrequency)

    else:
      total.add(currentfrequency)
      print (currentfrequency)
      switch = 1
      break
