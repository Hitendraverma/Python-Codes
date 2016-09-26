#!/usr/bin/python

import sys

try:
	#open file stream
	file = open(text.txt, "w")
except IOError:
	print "There was an error writing to", text.txt
	sys.exit()
print "Enter " , text.txt   


