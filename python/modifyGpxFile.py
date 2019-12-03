import sys
import re
import datetime

'''
Adds fake timestamps and elem index to trkpt tags in a .gpx file. 
Found a site that generated .gpx files without these, but needed these fields to simulate a trip on my phone, and editing 200+ lines manually is no bueno.
'''

if len(sys.argv) == 1:
  sys.exit("Not enough arguments specified.\nScript takes 1-2 arguments: first should be the .gpx file to modify. The 2nd (optional) is a subfolder to put the modified file into.")

gpx_filename = sys.argv[1]
save_folder = sys.argv[2] if len(sys.argv) > 2 else None

trkpt_pattern = "(<trkpt.*?)/>"
elem_count = 0
timestamp_format = "%Y-%m-%dT%H:%M:%SZ"
timestamp = datetime.datetime.strptime('1970-01-01T00:00:00Z', timestamp_format)

def get_save_filename(): 
  filename_no_extension = re.search("^[^.]*", gpx_filename).group(0)
  modified_filename = filename_no_extension + "_modified.gpx"
  if save_folder != None: 
    save_filename = save_folder + "/" + gpx_filename
  else: 
    save_filename = modified_filename
  return save_filename

def increment_indexes():
  global elem_count
  global timestamp
  elem_count = elem_count + 1
  timestamp = timestamp + datetime.timedelta(seconds=1)

def get_timestamp():
  return timestamp.strftime(timestamp_format)

def add_fake_data_to_row(row):
  row = re.sub(trkpt_pattern, "\\1><elem>" + str(elem_count) + "</elem>" + "<time>" + get_timestamp() + "</time></trkpt>", row)
  increment_indexes()
  return row

def read_file(filename):
  with open(filename, "r") as file:
    data = file.read()
    data = re.sub(trkpt_pattern, "\n\\1/>", data) #Just for pretty print, makes manual editing easier.
    return data.splitlines(keepends=True)

def save_to_file(data):
  with open(get_save_filename(), "w") as modified_file:
    for line in data:
      if line != None:
        modified_file.write(line)

data = read_file(gpx_filename)
modified_data = []
for line in data:
  modified_data.append(add_fake_data_to_row(line))

save_to_file(modified_data)
