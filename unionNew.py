#!/usr/bin/python

# -*- coding: UTF-8 -*-

def unionNew (L1,L2):
	'''
	 L1 & L2 are lists of the same length, n
	'''
	temp = []
	for i1 in L1:
		flag = False
		for i2 in L2:
			if i1 == i2:
				flag = True
				break
		if not flag:
			temp.append(i1)
	return temp + L2
	
	