import shutil
import os

def swapFileData():
    file1 = input("Enter the file name: ")
    file2 = input("Enter the name of file 2:")

    file1r=open(file1,'r')
    data_a =file1r.read()
    print(data_a)
    
    file2r=open(file2,'r')
    data_b=file2r.read()

    file1w=open(file1,'w')
    file1w.write(data_b)

    file2w=open(file2,'w')
    file2w.write(data_a)

swapFileData()    