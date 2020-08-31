#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
try:
	#可能会出现文件找不到的异常：FileNotFoundError
	file = open("d:/test.txt","r")
	#可能会出现类型异常：ValueError
	c = int(input("请输入整数选项："))
	print("用户输入了： %d" %c)
	
#指定需要处理多个异常类型，包含在一个元组中
except (FileNotFoundError,ValueError) as e:
	print("出现了一些异常：",e)
'''
'''
try:
	c = int(input("Please input choose: "))
	print("The user input is: %d" %c)
except ValueError as e:
	raise ValueError("类型转换错误")
	
'''
class MyException(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return "异常描述：%s" % self.message
try:
	#用户输入数据
	num1 = float(input("请输入第一个数据："))
	num2 = float(input("请输入第二个数据："))
	res = num1 / num2
# 处理类型异常
except ValueError:
	print("只能输入数字")
	raise MyException("只能输入数字，但是用户输入了其他非数字字符")
# 处理0除数异常
except ZeroDivisionError:
	print("0不能作为除数")
	raise MyException("亲，不能用0作为除数的")
# 正常结果
else:
	#打印展示结果
	print("除法运算结果： %.2f" %res)
finally:
	print("计算过程结束")
	