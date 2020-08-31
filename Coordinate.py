# -*- coding:UTF-8 -*- 
'''
Your task is to define the following two methods for the Coordinate class:

Add an __eq__ method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

For more on __repr__, see this SO post.
'''


class Coordinate(object):
	x = 0
	y = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def getX(self):
		# Getter method for a Coordinate object's x coordinate.
		# Getter methods are better practice than just accessing an attribute directly
		return self.x

	def getY(self):
		# Getter method for a Coordinate object's y coordinate
		return self.y

	def __str__(self):
		return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
		
	def __eq__(self):
		if self.x == self.y:
			return True
	
	def __repr__(self):
		
		c = '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
		return c

c = Coordinate(2,2)
print(c.__repr__())
print(c.getX())
print(c.__eq__())

print(eval(c.__repr__()))