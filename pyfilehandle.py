#!/usr/bin/python

#file handling in python ### File handling in python is very simple.

myfile=open("pytext.txt" , "w")
myfile.write("""This file is created from python code""")
myfile.close()
#for append "a"
myfile=open("pytext.txt", "a")
myfile.write("This is appended test in the file created by python code")
myfile.close()
#for read "r"
myfile=open("pytext.txt", "r")
read=myfile.read()
print read
myfile.close()
