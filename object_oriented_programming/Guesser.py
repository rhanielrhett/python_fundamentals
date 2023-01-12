#!usr/bin/env python

"""
Guess a number between 1 and 100
"""

import random
def main():
	print "Guess a number between 1 and 100"
	randomNumber = random.randint(1, 100)
	found = False

	while not found:
		userGuess = input("Your guess: ")

		if userGuess == randomNumber:
			print "You guessed it!"
			found = True

		elif userGuess > randomNumber:
			print "Guess lower"

		else:
			print "Guess Higher"

if __name__ == "__main__":
	main()