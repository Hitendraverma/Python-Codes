#!/usr/bin/python

count=0
name=input("Enter your name : ")
for letter in name:
	if (letter in ['A','E','I','O','U']):
		count=count+1
print("You have" , count , "vowel in your name")

