#!/usr/bin/python
# -*- coding: UTF-8 -*-


def union(L1,L2):
	'''
	L1 & L2 are list of the same length, n
	'''
	temp = L1[:]
	for i2 in L2:
		flag = False
		
		for i1 in temp:		#判读是否添加到temp部分
			if i2 == i1:     #如果相等，则不添加进去
				flag = True     #标志为，这代表不用添加
				break			#跳出此次循环,共有两种方法，走完or break
				
				
		if not flag:
			temp.append(i2)
	return temp

list1 = [1,3]
list2 = [2,5]


print(union(list1, list2))
