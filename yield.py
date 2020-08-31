#!/usr/bin/python

def genPrimeNum():
	prime_num =[]
	i = 2
	while True:
		n = 0
		l = len(prime_num)
		for num in prime_num:
			if i % num != 0:
				n += 1
		if n == l:
			prime_num.append(i)
			
			yield i
		i += 1
		
			
test = genPrimeNum()
print(test.next())
print(test.next())
print(test.next())
print(test.next())
print(test.next())
print(test.next())