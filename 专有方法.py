# -*- coding: UTF-8 -*-


'''
类的专有方法


'''
'''
class test:
	
	def def __init__(self):  # 构造函数，在生成对象时调用
		pass
		
	def __del__(self):
		pass
		
	def __repr__(self):
		pass
	
'''
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def __str__(self):
		return "Vector (%d, %d)" %(self.a, self.b)
		
	def __truediv__(self, other):  	#类的两个实例自己运算
		return Vector(self.a * other.a, self.b * other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 / v2)	 # 运算符号要和 __truediv__ 专有方法一致