# -*- coding: UTF-8 -*- 
'''
采用BFS广度优先算法找到所有路径，更改一下的话也可以输出最短路径，暂未考虑线路出现回路的情况

'''
# 首先定义线路结构图
graph = {"1": ["2","3","4"], "2": ["1","3","5"], "3": ["1","2","4","5","6"], "4": ["1","3","6","7"], "5": ["2","3","6"], "6":["3","4","5","7"],"7":["4","6"]}

# 下面是输出线路的结构图，分别打印每个节点的
'''
print("线路的连接图是：")
for i in graph.keys():
	print("graph[%s]: %s" %(i, graph[i]))
'''

# bsf 实现	
def bsf(graph, start , end):
	
	checked = []		#储存已经检查过的节点
	
	queue = [[start]] 	# 将起始节点存入队列中
	allPath = []
	
	#path =[start]		# 储存从开始节点到终点的路线列表
	
	if start == end:
		return "输入的起始节点：【%s】与末尾节点：【%s】一致，请检查节点输入是否正确。"%(start, end)
	
	while queue:       		# 如果队列中有节点
		path = queue.pop(0) #将队列中的第一个加入的路径取出
		#print(path)
		node = path[-1]
		#初始化完成
		if node not in checked:
			neighbours = graph[node]
			for neighbour in neighbours:
				new_path = list(path)
				
				new_path.append(neighbour)
				queue.append(new_path) 		
				if neighbour == end:
					allPath.append(new_path)				
			checked.append(node)
	
	if allPath:
		return allPath	
	return ("没有找到起点：【%s】 到 终点：【%s】 的路径，请检查节点是否正确" %(start, end))
		

path = bsf(graph, "1", "2")
print(path)
