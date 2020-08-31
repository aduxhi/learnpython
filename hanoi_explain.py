# -*- coding: UTF-8 -*- 
# 汉诺塔问题--经典递归问题--recursive

# n其实是A柱子剩余的盘子个数
# n 个盘子 a --> c
# n-1 个盘子 a ---> b
# 将剩余的 n = 1 , a --> c
# 再将 n-1 个盘子 从 b --> c
def hanoi(n, a, b, c):    
	if n == 1:
		print(a, '-->', c)				#a , c 代表的是【起点】和【终点】位置,因为传递过来的是改变顺序后的参数	
	else:						
		hanoi(n - 1, a, c, b)			# 把 n-1 从 a --> b
		print(a, '-->', c)				# 把最后的一个从a --> c; 
		hanoi(n - 1, b, a, c)			# 把剩下的从  b --> c



hanoi(2, 'A', 'B', 'C')
