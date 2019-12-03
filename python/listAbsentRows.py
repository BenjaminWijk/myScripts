import os
import sys

def get_file(filename):
    with open(filename) as f:
        return f.readlines()

#Loop through lines in compareFile. If any line isn't found in source, store that line
def findMissingFrom(source, compareFile):
  missingLines = []
  for line in compareFile:
    if line not in source:
      missingLines.append(line)
  return missingLines

#TODO: fix extra linebreak
def printMissing(filename, missingArray):
  if len(missingArray) == 0:
    print("No value missing from " + filename)
    return
  print("Values missing from " + filename + ":")
  for val in missingArray:
    print("  " + val[:-1]) #Remove linebreak character

file1_path = sys.argv[1]
file2_path = sys.argv[2]

file1 = get_file(file1_path)
file2 = get_file(file2_path)  
  
missingFrom1 = findMissingFrom(file1,file2)
missingFrom2 = findMissingFrom(file2,file1)

printMissing(file1_path, missingFrom1)
printMissing(file2_path, missingFrom2)


