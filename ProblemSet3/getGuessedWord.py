#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 返回已经猜到的单词
def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	
	returns: string, comprised of letters and underscores that represents
	  what letters in secretWord have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE...
	gussed = []
	for i in secretWord:
		if i in lettersGuessed:
			gussed.append(i)
		else:
			gussed.append('_ ')
	return ''.join(gussed)

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)

