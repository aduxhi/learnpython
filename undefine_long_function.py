# -*- coding: UTF-8 -*-

'''
def printinfo(arg1, *vartuple ):
	print("output: ")
	print(arg1)
	print(vartuple)
printinfo(70,60,"t5")
'''


def printinfo(arg1, *vartuple):
	print("output:")
	print("arg1 is: ", arg1)
	for var in vartuple:
		print(var)
	print(vartuple)
	return
	
printinfo(10,20,30)
