#!/usr/bin/python

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	  False otherwise
	'''
	# FILL IN YOUR CODE HERE...
	n = 0
	for i in secretWord:
		if i in lettersGuessed:
			n +=1
	if n == len(secretWord):
		return True
	else:
		return False

secretWord = 'eikps'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)
