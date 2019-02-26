file = open('Input.txt','r')
file = file.read()
data = [int(x) for x in file.split()]


def parse(data, metaentry):
  child, meta = data[:2]
  data = data[2:]

  for x in range(child):
    data, metaentry = parse(data, metaentry)

  if child == 0:
    metaentry.append(data[:meta])
    data = data[meta:]
    return data, metaentry
  else:
    metaentry.append(data[:meta])
    data = data[meta:]
    return data, metaentry


metaentry = []
parse(data, metaentry)

def sum_metaentry(metaentry):
  count = 0
  for x in metaentry:
    for y in x:
      count = count + y
  print(count)

sum_metaentry(metaentry)