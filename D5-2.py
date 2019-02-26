import sys
import string

sys.stdin = open('Input.txt','r')
for x in sys.stdin:
  polymer = x


'''Function to remove letters'''
def newstring(lower,upper):
  reducedpolymer = list(filter(lambda x: x!=lower and x!=upper, polymer))
  return reducedpolymer

'''Function to determine length of the polymer after removal of the letter and reduction'''
def lengthofpolymer(poly):
  finalpolymer = []
  for x in poly:
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
  return len(finalpolymer)

''' List of tuples to iterate over'''
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
lowerupper = list(zip(lowercase, uppercase))

shorteststring = []

for x,y in lowerupper:
  shorteststring.append(lengthofpolymer(newstring(x,y)))

print(min(shorteststring))








