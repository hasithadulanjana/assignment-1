import csv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))
ifile = open('H:/assigment/first.csv',"r")
read = csv.reader(ifile)
#for row in read:
    # print (row)
def get_id():

    for row in read:
        print(row[0],row[5])
        get_num=[]
        get_num.append(row[5])
        print(get_num)




get_id()

