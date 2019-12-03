import re
import os

pattern = re.compile(".*\.yml$")

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

#absolute path
path = os.getcwd()

ymlFiles = []
for file in os.listdir(path):
  if re.search(pattern, file) != None:
    ymlFiles.append(file)

schemaFiles = []

#Add additional foldernames here.
folders = []
folders.append("xsd")
folders.append("xslt")
folders.append("lookup_tables")
folders.append("jsonschema")

for foldername in folders:
  for file in os.listdir(path + "/" + foldername):
    schemaFiles.append(foldername + "/" + file)

blobYml = ""

for yml in ymlFiles:
  blobYml += file_get_contents(yml)

schemaNotInYml = []

for schema in schemaFiles:
  if(schema not in blobYml):
    print("removing " + schema)
    os.remove(schema)

  



