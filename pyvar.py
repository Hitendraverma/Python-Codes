#!/usr/bin/python

#Global and local variables in pyhton 

num1=200
def func():
	#num1=90
	global num1
	print"Local num" , num1
	return
func()
print"Global num",num1
