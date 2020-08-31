#!/usr/bin/python
# -*- coding: UTF-8 -*-
class binaryTree(object):    
	def __init__(self, value):        #初始化
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None 
		
	def setLeftBranch(self, node):
		self.leftBranch = node
	def setRightBranch(self, node):
		self.rightBranch = node
	def setParent(self, parent):
		self.parent = parent
	
	def getValue(self):
		return self.value
	def getLeftBranch(self):
		return self.leftBranch
	def getRightBranch(self):
		return self.rightBranch
	def getParent(self):
		return self.parent
		
	def __str__(self):                #默认返回值
		return str(self.value)
#-----------------------------------------------------		
# 设置好二叉树
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)

#定义一些行为
def find6(node):
	return node.getValue() == 6

def find10(node):
	return node.getValue() == 10

def find2(node):
	return node.getValue() == 2


def lt6(node):
	return node.getValue() > 6

#-----------------------------------------------------------------

def BFSBinary(node, fcn):
	queue = [node]
	while len(queue) > 0:
		print("at node: " + str(queue[0].getValue()))
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(0)
			if temp.getLeftBranch():					# 如果左支获得值
				queue.append(temp.getLeftBranch())		# 将获得的值加入到队列中
			if temp.getRightBranch():					# 如果右支获得值
				queue.append(temp.getRightBranch())		# 也直接加入到队列中
			
	return False
	
#print(BFSBinary(n5, find2))

# -------------------------------------------------------
# 深度优先算法
def DFSBinary(root, fcn):                
	queue = [root]    #储存树的队列
	while len(queue) > 0:
		print ('at node ' + str(queue[0].getValue()))
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(0)
			if temp.getRightBranch():					#如果右侧有分枝
				queue.insert(0, temp.getRightBranch())	# 将右侧分支节点插入到序列中的的第一
			if temp.getLeftBranch():					
				queue.insert(0, temp.getLeftBranch())	#将左侧这个点插入第一位置，这样就会把右侧之路覆盖
	return False

#-------------------寻找路径------------------
def DFSBinaryPath(root, fcn):
	queue = [root]
	while len(queue) > 0:
		if fcn(queue[0]):			#如果找到了这个终点
			return TracePath(queue[0])
		else:
			temp = queue.pop(0)
			if temp.getRightBranch():
				queue.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				queue.insert(0, temp.getLeftBranch())
	return False

								
def TracePath(node):			 # 寻找路径函数
	if not node.getParent():     # 如果这个节点的木节点不存在存在
		return [node]
	else:                        # 如果母节点存在
		return [node] + TracePath(node.getParent())	#[返回一个class 类型的列表]
		
	

'''
print('')
print ('DFS path')
pathTo6 = DFSBinaryPath(n5, find6)
print [e.getValue() for e in pathTo6]
'''


# 有序
def DFSBinaryOrdered(root, fcn, ltFcn):
	queue = [root]
	while len(queue) > 0:
		print ('at node ' + str(queue[0].getValue()))
		if fcn(queue[0]):
			return True
		elif ltFcn(queue[0]):
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.insert(0, temp.getLeftBranch())
		else:
			temp = queue.pop(0)
			if temp.getRightBranch():
				queue.insert(0, temp.getRightBranch())
	return False

print(DFSBinary(n5, find6))
print(BFSBinary(n5, find6))

print(DFSBinaryOrdered(n5, find6, lt6))