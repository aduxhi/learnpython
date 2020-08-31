#!/usr/bin/python

import string
coder = {"a":"c"}

'''
string.punctuation, plus the space (' ') and all numerical characters (0 - 9) found in string.digits
'''
def applyCoder(text, coder):
	"""
	Applies the coder to the text. Returns the encoded text.

	text: string
	coder: dict with mappings of characters to shifted characters
	returns: text after mapping coder chars to original text
	"""
	s1 = string.punctuation
	s2 = string.digits
	s3 = s1 + s2 + ' '
	text2 = []
	for letter in text:
		if letter not in s3:
			
			text2.append(coder[letter])
			
		else:
			text2.append(letter)
	text3 = "".join(text2)
	return text3
	
print(applyCoder("a!a a", coder))
			
		