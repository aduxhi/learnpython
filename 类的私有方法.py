# -*- coding: UTF-8 -*-
'''
类的方法和属性


__private_attrs:两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。使用方法：self.__private_attrs。
类的方法：
类的方法中必须包含参数 self, 且为第一个参数，self代表的是类的实例。

类的私有方法：
__private_method:两个下划线开头，声明该方法为私有方法，只能在类的内部调用，不能在类的外部调用

self.__priate_methods


'''
class JustCounter:
	__secretCount = 0 #si you bian liang
	publicCount = 0 # gong kai bian liang
	
	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)
		
counter = JustCounter()

counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount) #报错 has no attribute