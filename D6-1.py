import sys
import re
import numpy as np

'''Handle Input'''
sys.stdin = open('Input.txt','r')
coordinates = []
for x in sys.stdin:
  splitter = re.compile(r"\d+")
  coordinates.append(splitter.findall(x))
coordinates = [[int(x) for x in y] for y in coordinates]

''' calculate distance between two points'''
def distance(a,b,c,d):
  distance = abs(a-c) + abs(b-d)
  return int(distance)

'''Return index of shortest distance in the list. Returns -1 if it is the same distance from two points'''
def shortestdistance(listofdistance):
  if listofdistance.count(min(listofdistance)) == 1:
    return (listofdistance.index(min(listofdistance)))
  else:
    return (-1)

'''Return index of coordinates that are infinite'''
def infinity(cube):
  infinite = set()
  for x in cube[:,0]:
    infinite.add(int(x))
  for x in cube[0,:]:
    infinite.add(int(x))
  for x in cube[:,-1]:
    infinite.add(int(x))
  for x in cube[-1,:]:
    infinite.add(int(x))
  return infinite

'''return dictionary of index:count of each coordinate not in infinity'''
def mostcommon(matrix):
  unique_elements, count_elements = (np.unique(matrix, return_counts=True))
  return (list(zip(unique_elements,count_elements)))

'''create new matrix'''
matrix = np.zeros((400,400))
for (x,y), value in np.ndenumerate(matrix):
  distances = []
  for pair in coordinates:
    distances.append(distance(pair[0],pair[1],x,y))
  matrix[y,x] = shortestdistance(distances)


matrix = matrix.astype(int)
infinite = infinity(matrix)
mostcommon = mostcommon(matrix)
answer = []

'''remove infinite answers from mostcommon'''
for x,y in mostcommon:
  if int(x) not in infinite:
    answer.append(y)



print(max(answer))






'''create new matrix'''
'''matrix = np.zeros((50,50))
for (x,y), value in np.ndenumerate(matrix):
  distances = []
  print ('matrix coordinate:', x,y)
  for pair in coordinates:
    distances.append(distance(pair[0],pair[1],x,y))
    print ('distance:', distance(pair[0],pair[1],x,y))
    print (pair[0],pair[1],x,y)
  print ('shortest distance:',shortestdistance(distances))
  matrix[y,x] = shortestdistance(distances)
  print ("")
matrix = matrix.astype(int)'''

