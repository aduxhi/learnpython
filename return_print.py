# -*- coding: UTF-8 -*-
'''
the print() function writes, i.e., "prints",a string in the console. The return statement causes your function to exit and hand back a value to its caller.(使函数终止并且返回一个值给它的调用者) The point of functions in general is to take in inputs and return something. The return statement is used when a function is ready to return to its caller.
Fox example, here's a function utilizing both print() and return.
'''

def foo():
	print("hello form inside of foo")
	return 1
	
print("going to call foo: ")

x = foo()  	# 调用foo(),将返回值赋予 x

print("called foo")

print("foo returned " + str(x))
print(foo()) # 调用 foo()

print(foo)		#
print(type(foo))