import sys
import re
import numpy as np

'''Edges (a --> b) '''
sys.stdin = open('Test.txt','r')
edges = []
for x in sys.stdin:
  splitter = re.compile(r"[A-Z]")
  edges.append(splitter.findall(x))
for x in edges:
  del x[0]

'''Determine all source vertexes'''
def findsource(edges):
  vertex = set()
  endpoint = set()
  output = []
  for edge in edges:
    vertex.add(edge[0])
    endpoint.add(edge[1])
  for x in vertex:
    if x not in endpoint:
      output.append(x)
  return output

'''Is Indegree One?'''
def indegree(letter):
  count = 0
  for x in edges:
    if x[1] == letter:
      count = count + 1
      if count > 1:
        return False
  return True


'''List of vertexes to add to Final, remove edges from edges. Sorted is reversed because it needs to be appended to the beginning of Sourcevertex later'''
def newlist(sourcevertex):
  vertexes = []
  for x in edges[:]:
    if x[0] == sourcevertex:
      if indegree(x[1]) == True:
        vertexes.append(x[1])
        print(vertexes)
      edges.remove(x)
  return sorted(vertexes, reverse=True)

Final = []
Sourcevertex = sorted(findsource(edges))

print (edges)

print (Sourcevertex)

while Sourcevertex != []:
  tempsource = (Sourcevertex.pop(0))
  print('tempsource = ' + tempsource)
  Final.append(tempsource)
  newverticies = newlist(tempsource)
  for x in newverticies[:]:
    Sourcevertex.insert(0, newverticies.pop(0))
    print ('Sourcevertex = ', Sourcevertex)

print (Final)








