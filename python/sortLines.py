import sys

filename = sys.argv[1]

def getFileLines(filename):
  lines = [] 
  for line in open(filename):
    lines.append(line)
  return lines

fileLines = getFileLines(filename)
fileLines.sort()

for line in fileLines:
  print(line)


