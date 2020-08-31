# -*- coding: UTF-8 -*-
def myLog(x, b):
	'''
	x: a positive integer
	b: a positive integer; b >= 2

	returns: log_b(x), or, the logarithm of x relative to a base b.
	'''
	# Your Code Here
	n = 0
	for i in range(x):
		if b**i <= x:
			if i > n:
				n = i
		else:
			break
			
	return n
	
myLog(15, 3)
		