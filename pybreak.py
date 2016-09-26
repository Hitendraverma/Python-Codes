#!/usr/bin/python

var=1 
while(var<=15):
	if(var==10):
		break
	print(var)
	var=var+1

print("Good bye")

while True:
	print("Enter a digit : ")
	num=input()
	var=str(num)
	if(ord(var) in range(48,58)):
		break
print("You Entered in range")

