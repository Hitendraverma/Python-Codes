#!/usr/bin/python
#Nested IF ELSE loop

char=input("Enter any Char : ")
#Give input in quotes
if ord(char)>=65 and ord(char)<=90:
	print("You entered upper case")
	if char in ['A','E','I','O','U']:
		print("You entered a vowel")
	else:
		print("You Entered a consonant")

elif ord(char)>=97 and ord(char)<=122:
	print("You Entered a lower case")
	if char in ['a','e','i','o','u']:
		print("You Entered a Vowel")
	else: 
		print("You Entered a consonant")

else:
	print("Its not a Alphabet")
