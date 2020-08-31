#!/usr/bin/python
def laceStrings(s1, s2):
	"""
	s1 and s2 are strings.

	Returns a new str with elements of s1 and s2 interlaced,
	beginning with s1. If strings are not of same length, 
	then the extra elements should appear at the end.
	"""
	# Your Code Here
	ma = max (len(s1),len(s2))
	mi = min (len(s1),len(s2))

	l3=[]
	for i2 in range(mi):
		l3.append(s1[i2])
		l3.append(s2[i2])
	if len(s1) > mi:
		
		l3.append(s1[mi:])
	if len(s2) > mi:
		
		l3.append(s2[mi:])
	return ''.join(l3)

s1 = 'abcd' 
s2 = 'efghi'
	
print laceStrings(s1, s2) 						#'aebfcgdhi'




