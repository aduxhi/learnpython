# -*- coding: UTF-8 -*-

class binaryTree(object):
	#initial    
	def __init__(self, value):        #初始化
		self.value = value			  #只会设定自己的值
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None 
	#set	
	def setLeftBranch(self, node):
		self.leftBranch = node
	def setRightBranch(self, node):
		self.rightBranch = node
	def setParent(self, parent):
		self.parent = parent
	#get	
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


## make a decision tree
## for efficiency should really generate on the fly, but here will build
## and then search
#treeTest = buildDTree([], [a,b,c,d])

def buildDTree(sofar, todo):
	if len(todo) == 0:			
		return binaryTree(sofar)								# 创建一个二叉树实例
	else:
		withelt = buildDTree(sofar + [todo[0]], todo[1:])		# sofar 是一个列表，todo也是一个列表
		withoutelt = buildDTree(sofar, todo[1:])				# 
		
		here = binaryTree(sofar)								# here 二叉树的一个实例
		here.setLeftBranch(withelt)
		here.setRightBranch(withoutelt)
		return here


#--------------------------------------------------------------------------------


def DFSDTree(root, valueFcn, constraintFcn):
	queue = [root]
	best = None
	visited = 0
	while len(queue) > 0:
		visited += 1
		if constraintFcn(queue[0].getValue()):
			if best == None:
				best = queue[0]
				print best.getValue()
			elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
				best = queue[0]
				print best.getValue()
			temp = queue.pop(0)
			if temp.getRightBranch():
				queue.insert(0, temp.getRightBranch())				#堆栈
			if temp.getLeftBranch():
				queue.insert(0, temp.getLeftBranch())
		else:
			queue.pop(0)
	print 'visited', visited
	return best




#---------------------------------------------------------
def BFSDTree(root, valueFcn, constraintFcn):
	queue = [root]
	best = None
	visited = 0
	while len(queue) > 0:
		visited += 1
		if constraintFcn(queue[0].getValue()):
			if best == None:
				best = queue[0]
				print best.getValue()
			elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
				best = queue[0]
				print best.getValue()
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())			# 序列
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())			
		else:
			queue.pop(0)
	print 'visited', visited
	return best  

#----------------------------------------------------------------
#定义决策树和一些评估函数
a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]

def sumValues(lst):					# 计算lst列表中的所有值的和
	vals = [e[0] for e in lst]
	return sum(vals)

def sumWeights(lst):				#计算lst列表中的所有重量
	wts = [e[1] for e in lst]
	return sum(wts)

def WeightsBelow10(lst):			#列表中的总的质量是否小于10
	return sumWeights(lst) <= 10

def WeightsBelow6(lst):				#列表中所有值的总质量是否小于6
	return sumWeights(lst) <= 6
#-----------------------------------------------------------------

treeTest = buildDTree([], [a,b,c,d])

print ''
print 'DFS decision tree'
foobar = DFSDTree(treeTest, sumValues, WeightsBelow10)
print foobar.getValue()

print ''
print 'BFS decision tree'
foobarnew = BFSDTree(treeTest, sumValues, WeightsBelow10)
print foobarnew.getValue()
