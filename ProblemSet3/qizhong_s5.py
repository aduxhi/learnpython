# -*- coding: UTF-8  -*-

'''
Suppose you are given two strings (they may be empty), s1 and s2. You would like to "lace" these strings together, by successively alternating elements of each string (starting with the first character of s1). If one string is longer than the other, then the remaining elements of the longer string should simply be added at the end of the new string. For example, if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.
Write an iterative procedure, called laceStrings(s1, s2) that does this.
'''

def laceStrings(s1, s2):
	
	"""
	s1 and s2 are strings.
	Returns a new str with elements of s1 and s2 interlaced,
	beginning with s1. If strings are not of same length, 
	then the extra elements should appear at the end.
	"""	
		
	ma = max (len(s1),len(s2))
	mi = min(len(s1),len(s2))

	l3=[]
	for i2 in range(mi):
		l3.append(s1[i2])
		l3.append(s2[i2])
		
	
	if len(s1) > mi:
		print s1[mi:]
		l3.append(s1[mi:])
	if len(s2) > mi:
		print s2[mi:]
		l3.append(s2[mi:])
	return l3

 			
s1 = 'abcdpr'
s2 = 'efghi'
print laceStrings(s1, s2)

