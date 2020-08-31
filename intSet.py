# -*- coding: UTF-8 -*-

""" 
intSet is a set of integers
The value is represented by a list of ints, self.vals.
Each int in the set occus in self.vals exactly once.
"""
class intSet(object):
	def __init__(self):
		self.vals = []
	
	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)
			
	def member(self, e):
		return e in self.vals
	
	def remove(self, e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')
	
	def __str__(self):						
		self.vals.sort()
		return '{' + ', '.join([str(e) for e in self.vals]) + '}'
		
s = intSet()
print (s)
s.insert(5)
s.insert(4)
s.insert(3)
print(s)
print(s.member(3))
print(s.member(5))
print(s.member(6))
print(s)
s.remove(3)
#s.remove(3)
print(s.__str__())
print(s.__init__())

