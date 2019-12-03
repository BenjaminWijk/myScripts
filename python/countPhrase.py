import re
import os
import sys

pattern = re.compile(sys.argv[1])
count = 0

def get_file(filename):
    with open(filename) as f:
        return f.readlines()

def matches_pattern(line):
    if re.search(pattern,line) != None:
        return True
    return False

#absolute path
path = os.getcwd()

#Add relative path if specified. Search specific file if path does not end on "/", otherwise search folder
additionalPathInfo = ""
if len(sys.argv) >= 3:
    additionalPathInfo = sys.argv[2]
    path += "/" + additionalPathInfo

filesToSearch = []

if not additionalPathInfo.endswith("/"):
    filesToSearch.append(get_file(additionalPathInfo))
else:
    for file in os.listdir(path):
        #Don't search in script
        if file == sys.argv[0]:
            continue
        filePath = additionalPathInfo + file
        if not os.path.isfile(filePath):
            continue
        filesToSearch.append(get_file(filePath))

print("Number of files to search:" + str(len(filesToSearch)))
for file in filesToSearch:
    for line in file:
        if matches_pattern(line):
            count = count+1

print("The phrase \""+ sys.argv[1] + "\" was found " + str(count) + " times.")



