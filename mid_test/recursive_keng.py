#!/usr/bin/python

t = {}

def ex(x):
	global t
	if x > 1:
		x -= 1
		t[x] = ex(x)
	else:
		return x

(ex(10))
print(t)