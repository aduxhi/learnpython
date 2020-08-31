def isln(a,s):
	'''
	a is a character, or,singleton string.
	s is a string, sorted in alpahbetical order.
	'''
	
	if len(s) == 0:
		                
		return False
	elif len(s) == 1:
		return a == s[0] 
	else:
		
		test = s[len(s)/2]
		
		if test == a:
			return True
		elif a < test:
			return isln(a, s[ :len(s)/2])
		else:
			return isln(a, s[len(s)/2+1: ])

list1=['a','b']


#print ('a' == list1[0])
print (isln('c',list1))

			