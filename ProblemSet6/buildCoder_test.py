#!/usr/bin/python
import string
shirt = 9
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase

	
d1 = {}
d2 = {}
d11 = {}
d22 = {}
i = 0
for letter in s1:
	d1[i] = letter
	i += 1
for letter in s1:
		d11[letter] = i
		i += 1
	
i = 0
for letter in s2:
	d2[i] = letter 
	i += 1
	
for n in d1:
	if n + shirt < 26:
		d11[d1[n]] = d1[n+shirt]
	else: 
		d11[d1[n]] = d1[n+shirt-26]
	
print d11

s5 = string.punctuation
s6 = string.digits
s7 = s5 + s6 + ' '


text2 = ''
for letter in text2:
		if letter not in s3:
			text2.append(coder[letter])
			
		else:
			text2.append(letter)
			
print text2