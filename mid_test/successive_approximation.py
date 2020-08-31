#!/usr/bin/python
'''
Successive approximation is a general method in which on each iteration of an algorithm, we find a closer estimate of the answer for which we are seeking. One class of successive approximation algorithms uses the idea of a fixed point. If f(x) is a mathematical function, then finding the x such that f(x) = x gives us the fixed point of f.

One way to find a fixed point is to start with some guess (e.g. guess = 1.0) and, if this is not good enough, use as a next guess the value of f(guess). We can keep repeating this process until we get a guess that is within epsilon of f(guess).

Here is a slightly incorrect definition of this function:
'''


def fixedPoint(f, epsilon):
	
	"""
	f: a function of one argument that returns a float
	epsilon: a small float

	returns the best guess when that guess is less than epsilon 
	away from f(guess) or after 100 trials, whichever comes first.
	"""
	guess = 1.0
	for i in range(100):
		
		if (abs(f(guess) - guess) < epsilon):
			return guess
		else:
			guess = f(guess)
	return guess


#-------------------------------------------
def sqrt(a):
	
	def tryit(x):
		return 0.5 * (a/x + x)
	
	return fixedPoint(tryit, 0.0001)



#print(sqrt(9))


#---------------------------------------------
def babylon(a):
	
	def test(x):
		return 0.5 * ((a / x) + x)
	
	return test

def sqrt(a):
	return fixedPoint(babylon(a), 0.0001)





#----------------------------------------------
print(sqrt(9))