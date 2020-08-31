def iterPower(a,b):
	resulut =1
	while b > 0:
		resulut *=a
		b -= 1
	return resulut
	
print(iterPower(2, 3))

def recurPower(a,b):
	print (a,b)
	if b == 0:
		return 1
	else:
		return a * recurPower(a, b-1)
		
print(recurPower(2, 4))
