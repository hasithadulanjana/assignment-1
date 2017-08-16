import csv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))
ifile = open('H:/assigment/first.csv', "r")
read = csv.reader(ifile)

#for row in read:
#  print (row)
"""
def get_data():
  for row in read:
        print(row[0:6])
get_data()
"""

def get_id():
     empolyeeids = []
     for row in read:
           employee = row[0]
           empolyeeids.append(employee)
           print(empolyeeids)


get_id()
