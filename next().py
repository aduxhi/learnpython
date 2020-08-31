# -*- coding: UTF-8 -*-

def fab(x):
	a, b, n, = 0, 1, 0

	while n < x:
		yield b
		a, b = b, a+b
		
		n += 1
	print ("done")
# 函数实例化	
f = fab(5)

print(type(fab))

print(type(f))

# 把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for i in f:
	print(i)
	
def odd():
	print('step 1')
	yield 1		#类似于return ,会返回函数的一个值，但不是结束函数，而是中断到这里
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

o = odd()	
next(o)	 
next(o)
print(next(o))



