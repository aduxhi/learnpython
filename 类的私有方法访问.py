# -*- coding: UTF-8 -*- 




class Site:
	def __init__(self, name, url):
		self.name = name	#public
		self.__url = url   #private
	def who(self):
		print("name: ",self.name)
		print("url: ",self.__url)
		
	def __foo(self):
		print("这是私有方法哦😯")
		
	def foo(self):					#用公开方法访问私有方法。。
		print("这是公开方法")
		self.__foo()
		
		
x = Site("菜鸟教材", "www.runoob.com")
x.who()
x.foo()
#x.__foo(）# 直接访问私有方法，报错