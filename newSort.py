#!/usr/bin/python
# -*- coding: UTF-8 -*-

def mySort(L):
	clear = False
	while not clear:
		clear = True
		
		for j in range(1, len(L)):
			
			if L[j-1] > L[j]:  # 如果前者大于后者
				
				clear = False  # 允许进入while循环
				
				temp = L[j]
				L[j] = L[j-1]
				L[j-1] = temp
				
				

def newSort(L):
	for i in range(len(L) - 1):
		
		j=i+1
		
		while j < len(L):
			
			if L[i] > L[j]: #如果L
				
				temp = L[i]
				L[i] = L[j]
				L[j] = temp
			
			j += 1
			
L = [3,1,2]

(mySort(L))
print L
#(mySort(L))