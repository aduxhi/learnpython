# -*- coding: UTF-8 -*-

#定义节点结构，包含节点
class Node(object):
	def __init__(self,number):
		self.number = number        # 节点的编号
		self.rchild = None			# 节点的右支
		self.lchild = None			# 节点的左支

'''
由于这里只是单纯的二叉树，而不是排序二叉树，所以不需要考虑数的大小关系等，
也就是说可以按先后顺序插入顺序可以设计成root,root->left,root-rght这样，
好处在于，root插入后，root左右为空，这时插入root->left,然后再是root->right，
这样能够确保root的2个子节点都有值，而不至于绕过root->rigth直接插入root->left->left这样的异常情况出现。
基于这样的设计，我们使用list来存储任意子节点为空的节点，换句话说，只要你这个节点不是左右节点都存在的情况下，
我下次插入节点就会考虑你。具体实现我们使用list来模拟队列，root,root->left,root->right依次入队，

接下来就是核心问题，怎么把增加新节点，第一步当然要先判断树是否为空



add基本的逻辑就是利用队列依次保存未满状态的节点，然后通过不断取队头来添加左右孩子，
并把左右孩子加入队列，插入完后检查是否走有孩子都有了，依然未满，则保留，满了，则退出队列取下一个队首。




 add基本的逻辑就是利用队列依次保存未满状态的节点，然后通过不断取队头来添加左右孩子，并把左右孩子加入队列，插入完后检查是否走有孩子都有了，依然未满，则保留，满了，则退出队列取下一个队首。
--------------------- 
作者：jchen104 
来源：CSDN 
原文：https://blog.csdn.net/wzngzaixiaomantou/article/details/81294915 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

class Tree(object):
	lis = []								#保存节点的列表
	def __init__(self):			
		self.root = None					#空值，初始化
		
	def add(self, number):
		node = Node(number)					#实例化一个节点
		if self.root == None:  				#判断节点的根是否为空，如果是，它就作为根节点
			self.root = node				# 确定根节点啦
			Tree.lis.append(self.root) 		#--入队列-- 将第一个add 的数作为根节点 储存根节点到队列中
		else:						   		#如果不是根节点
			while True:
				point = Tree.lis[0]   		#队列中的第一个点为父节点
				if point.lchild == None:
					point.lchild = node
					Tree.lis.append(point.lchild) 	# 继续入队列
					return							#退出函数
				elif point.rchild == None:
					point.rchild = node
					Tree.lis.append(point.rchild) 	# 继续入队列
					Tree.lis.pop(0)					#---出队列--节点装满了，弹出，这个一个队列形式，先进先出，与堆栈的后进先出还是有区别的
					return							#退出 add 函数
					
		
if __name__ =="__main__":
	t = Tree()
	L = [1,2,3,4,5,6,7]
	for x in L :
		t.add(x)
		
		print("success")
		
print(t)
		
		
