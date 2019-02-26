import sys

sys.stdin = open('Input.txt','r')
for x in sys.stdin:
  polymer = x

finalpolymer = []

for x in polymer:
  if len(finalpolymer) == 0:
    finalpolymer.append(x)
  else:
    if x.islower():
      if finalpolymer[-1] == x.upper():
        del finalpolymer[-1]
      else:
        finalpolymer.append(x)
    if x.isupper():
      if finalpolymer[-1] == x.lower():
        del finalpolymer[-1]
      else:
        finalpolymer.append(x)

print(len(finalpolymer))

