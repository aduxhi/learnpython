#!/usr/bin/python
# -*- coding: UTF-8 -*-
def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE...
	retlist = []		#   返回列表，没有被猜测的都可以
	import string
	abcList = string.ascii_lowercase

	for i in abcList:
		if i not in lettersGuessed:
			retlist.append(i)
	return ''.join(retlist)
	
#test code
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
