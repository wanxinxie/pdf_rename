# -*- coding: utf-8 -*-
from pdfrw import PdfReader
import os
import glob


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
Filename = os.path.join(THIS_FOLDER, 'target.zip')
renamedfilename =os.path.join(THIS_FOLDER, 'renamed.zip')
"""**Step 2:**
Determine new names

Change Filename to the zip file name you are working with
"""

# Change Filename below to the zip file name you are working with

# Determine new name

from os import walk
mypath = THIS_FOLDER + '/target'
f = []
d = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
f.remove('.DS_Store')
for file in f:
    d.append(THIS_FOLDER + '/target/'+file)
print(f)
print(d)


newnames = []
for i in range(len(f)):
  reader = PdfReader(d[i])
  title=''
  author=''
  date=''
  if str(type(reader.Info.Title)) != "<class 'NoneType'>":
    title= reader.Info.Title[1:len(reader.Info.Title)-1]
    print(title)
  if str(type(reader.Info.Author)) != "<class 'NoneType'>":
    author = reader.Info.Author[1:len(reader.Info.Author)-1]
    words = author. split()
    lastname = words[-1]
    print(lastname)
  if str(type(reader.Info.CreationDate)) != "<class 'NoneType'>":
    date = reader.Info.CreationDate[3:7]
    print(date)
  new_name = title +'|' + author + '|' + date +'.pdf'
  print(new_name)
  newnames.append(THIS_FOLDER + '/target/'+new_name)
count=0

"""Rename files"""

print(newnames)

for i in range(len(f)):
  os.rename(d[i],newnames[i])

"""Create new zip file with renamed pdf"""

