#!/usr/bin/python

'''wrd=raw_input("Enter a string : ")
rev=wrd[::-1]

print wrd
print rev
if wrd == rev :
	print "word is a palindrome"
else:
	print "Not a palindrome"
'''
#Even no.

a = [1, 4, 100, 9, 16, 25, 36, 49, 64, 81]
print a
'''
evn_list = []
new_list = [n for n in a if n % 2 == 0]


for alist in a :
    if alist % 2 == 0:
	evn_list.append(alist)
'''
#Now lets use power of python for above code

evn_list = [ alist for alist in a if alist % 2 == 0 ]
print evn_list
print (sorted(evn_list))
