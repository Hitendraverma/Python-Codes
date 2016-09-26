#!/usr/bin/python
import time
# functions in python 
a=input("Enter a : ")
b=input("Enter b : ")
def calculator(a,b):
	print"Addition : ", a+b
	var=a**b
	print"Function print"
	return var

var=calculator(a,b)
print"a power b : " , var

# function pass by value vs Reference 
#In python actual objects are passed 

empl={'alex':1500,'John':1200}
print"Employee list before update", empl
def newemp(empl):
	new={'Amar':1234 , 'Stan':123}
	empl.update(new)
	print"Employee updated list in Function" , empl
	return
newemp(empl)
print"Employee list update outside function" , empl

def emplist(empl):
	empl={'Gorge':1290,'frank':1009}
	print"Employee list 2 " , empl
	return
emplist(empl)

#Function with multiple variable lenth passed
time.sleep(2)
print"Function with multiple variables passed"
def display(*list):
	for listd in list:
		print(list)
	return
var=input()
display(var)

