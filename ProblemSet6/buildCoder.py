#!/usr/bin/python

import string

def buildCoder(shift):
	"""
	Returns a dict that can apply a Caesar cipher to a letter.
	The cipher is defined by the shift value. Ignores non-letter characters
	like punctuation, numbers, and spaces.

	shift: 0 <= int < 26
	returns: dict
	"""
	s1 = string.ascii_lowercase
	s2 = string.ascii_uppercase

	
	d1 = {}
	d2 = {}
	d11 = {}
	d22 = {}
	i = 0
	for letter in s1:
		d1[i] = letter
		i += 1
	for letter in s1:
			d11[letter] = i
			i += 1
	
	i = 0
	for letter in s2:
		d2[i] = letter 
		i += 1
	
	for n in d1:
		if n + shift < 26:
			d11[d1[n]] = d1[n+shift]
		else: 
			d11[d1[n]] = d1[n+shift-26]
	
	for n in d2:
		if n + shift < 26:
			d22[d2[n]] = d2[n+shift]
		else: 
			d22[d2[n]] = d2[n+shift-26]
			
	dictMerged=dict(d11)
	dictMerged.update(d22)
	
	return dictMerged

print(buildCoder(3))