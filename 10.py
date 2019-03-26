import re
import matplotlib.pyplot as plt
import numpy as np

file = open("10.txt","r")
data = []

for line in file:
    data.append(line)
    
for index, item in enumerate(data):
    item = re.findall('-?\d+', item)
    data[index] = [int(x) for x in item]


def xaxis(time):
    xaxis = []
    for line in data:
        x = line[0] + (line[2] * time)
        xaxis.append(x)
    return (xaxis)
    
    
def yaxis(time):
    yaxis = []
    for line in data:
        y = (line[1] * -1 + (line[3] * time * -1))
        yaxis.append(y)
    return (yaxis)

def when(maxtime):
    time = []
    for second in range(maxtime):
        time.append((np.std(xaxis(second))) + (np.std(yaxis(second))))
    return time.index(min(time))
        

def chart(seconds):
    plt.plot(xaxis(seconds),yaxis(seconds), 'ro')
    plt.show()
    
chart(10304)
