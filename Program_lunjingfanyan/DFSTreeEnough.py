#-------------------------------------------------------------------
def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
	stack = [root]
	best = None
	visited = 0
	while len(stack) > 0:
		visited += 1
		if constraintFcn(stack[0].getValue()):
			if best == None:
				best = stack[0]
				print best.getValue()
			elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
				best = stack[0]
				print best.getValue()
			if stopFcn(best.getValue()):
				print 'visited', visited
				return best
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)
	print 'visited', visited
	return best
#-----------------------------------------------------------------------------
def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
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
			if stopFcn(best.getValue()):
				print 'visited', visited
				return best
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
		else:
			queue.pop(0)
	print 'visited', visited
	return best

def atLeast15(lst):
	return sumValues(lst) >= 15

print ''
print 'DFS decision tree good enough'
foobar = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
								   atLeast15)
print foobar.getValue()

print ''
print 'BFS decision tree good enough'
foobarnew = BFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
									  atLeast15)
print foobarnew.getValue()



#--------------------------------------------------------------------------------
def DTImplicit(toConsider, avail):
	if toConsider == [] or avail == 0:
		result = (0, ())
	elif toConsider[0][1] > avail:
		result = DTImplicit(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
		withVal += nextItem[0]
		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
		if withVal > withoutVal:
			result = (withVal, withToTake + (nextItem,))
		else:
			result = (withoutVal, withoutToTake)
	return result

stuff = [a,b,c,d]

val, taken = DTImplicit(stuff, 10)

print ''
print 'implicit decision search'
print 'value of stuff'
print val
print 'actual stuff'
print taken

#-------------------------------------------------------------------------------
def DFSBinaryNoLoop(root, fcn):
	queue = [root]
	seen = []
	while len(queue) > 0:
		print 'at node ' + str(queue[0].getValue())
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(0)
			seen.append(temp)
			if temp.getRightBranch():
				if not temp.getRightBranch() in seen:
					queue.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				if not temp.getLeftBranch() in seen:
					queue.insert(0, temp.getLeftBranch())
	return False


##comment out

#n3.setLeftBranch(n5)
#n5.setParent(n3)

# run DFSBinary(n5, find6)




										 
