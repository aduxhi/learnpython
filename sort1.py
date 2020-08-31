#!/usr/bin/python

# -*- coding: UTF-8 -*- 

def selSort(L):
	for i in range(len(L)-1):   # 最后一个不用排了
		minIndx = i
		minVal = L[i]
		j = i + 1
		while j < len(L):   	# 找出i 后面最小的
			if minVal > L[j]:	#如果 L[i]不是最小的
				
				minIndx = j
				minVal = L [j]
				
			j += 1
			
		if minIndx != i:   		#如果后面有更小的
			temp = L[i]
			L[i] = L[minIndx]
			L[minIndx] = temp
			
			
def newSort(L):
	for i in range(len(L)-1):
		j = i + 1
		while j < len(L):
			if L[i] > L[j]:
				temp = L[i]
				L[i] = L[j]
				L[j] = temp
				
			j += 1

			
			