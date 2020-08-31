# -*- coding: UTF-8 -*-

'''
lis = []
for i in range(1,11):
	lis.append(i)

it = iter(lis)
for x in it:
	print(x, end = ' ')
	
print("\n")
	
import sys
lis2 = [1, 2, 3, 4]
it =iter(lis2)

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()
		
'''		
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 20:
			
		
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration
		
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))