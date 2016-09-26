#!/usr/bin/python

str1="hi this is capitalize() function of python"
print(str1.capitalize())
str2="""This is the demo for 
python string
showing count function
this show how many time a word is present """

print(str2.count('this'))

str3="urltest.com"
print(str3.endswith('.org'))
print(str3.endswith('.com'))

str4="Catch me if you can"
print"get the index position of y :" , str4.find('you')
#check all character in lower case
str5="hello python , this islower()"
print(str5.islower())
#check all chaacter are in upper case
str6="THIS IS UPPER CASE"
print(str6.isupper())
#to get length of a string

print("str6 length " , len(str6))

#to convert string in lower case 
print("str6 to lower" , str6.lower())
print("str5 to upper" , str5.upper())

# lstrip,rstrip and strip to remove bunch of any character from left/right side o a string 

str7="!!!!!!Whats up?"
print"this is lstrip", str7.lstrip('!')
str8="Its Collllllllllllllll"
print"this is rstrip" , str8.rstrip('l')
str88="!!!!Whats Up dude,, this is cool!!!!!!!"
print"This is strip : ", str88.strip('!')

#replace a word in string.
str9="This is blue mix"
print"replace function() :" , str9.replace('blue','black')

#split function()
str10="Tom Cruise"
print"this is split func :" , str88.split()
str11="I love PYTHON"
print"swap case () :" ,  str11.swapcase()



