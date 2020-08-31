#!/usr/bin/python

a, b = 0 , 1
while a < 1000:
	print(a, end=',')
	a, b = b, a+b

\

a, b = 0 , 1
while a < 1000:
	print(a)
	a, b = b, a+b