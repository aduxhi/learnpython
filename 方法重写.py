# -*- coding: UTF-8 -*-
class Parent:
	def myMethod(self):
		print("调用父类方法")
class Child(Parent):
	def myMethod(self):
		print("调用字类方法")

c = Child()
c.myMethod()
super(Child,c).myMethod() #用子类对象调用父类已经被覆盖的方法 super(super_Class_name,insatan_name).super_class_name

