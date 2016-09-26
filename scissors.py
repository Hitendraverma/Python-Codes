#!/usr/bin/python
import sys

#Its a simple two player game.
'''Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

p1 = input("Enter first player name : ")
p2 = input("Enter 2nd player name : ")

p1a = input(" Enter your option : ")
p21= input(" Enter your option : ")

def compare(u1,u2):
	if u1 == u2:
	   return("Game tie")
		elif u1 == 'rock' and u2 == 'scissors':
	         		return("Rock win")
	       		else:
				return("Paper Win")
        	elif u1 == 'scissors':
			if u2 == 'paper':
				return("scissors win")
			else: 
				return("Rock win")
		elif u1 == 'paper'
			if u2 == 'rock':
				return("paper win")
			else:	
				return("scissors win")
	else:
		return("Play again")
		sys.exit()

print (compare(p1a,p2a))
