#!/usr/bin/python
# -*- coding: UTF-8 -*- 
'''
	# Your code here
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		return True
	elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
		return True
	else:
		return False
		
print(isVowel('i'))
print(isVowel('b'))
'''

'''
As we'll see in subsequent lectures, everything in Python is an object(对象). Objects are special because we can associate special functions, referred to as object methods, with the object. In this problem you'll be working with string objects, and their built-in methods.

A complete description of the methods available to string objects can be found in the Python library reference on string methods. Another useful resource about string methods can be found here.

In this exercise, we want you to get some experience in using methods as functions. The convention for object methods is to use the "dot" notation, so that if s is a string, evaluating s.upper will return the actual function, and evaluating s.upper() will cause the function itself to be evaluated (in this case it returns a new string, since strings are immutable) with every character now in upper case. An example of this follows:
'''

s = 'abc'
print(s.capitalize)

print(s.capitalize())

str1 = 'exterminate!' 
str2 = 'number one - the larch'
str3 =str1.upper()
print(str1.upper)
print (str1.upper())
print(str1)
print(str1.isupper())
print(str3.isupper())

print(str1.islower())
str2 = str2.capitalize()
print(str2)

print("str2.swapcase",str2.swapcase())
print(str1.index('e'))
print(str2.index('n'))
print(str2.find('!'))
print(str1.count('e'))
str1=str1.replace('e', '*')
print str1
print(str2.replace('one', 'seven'))
