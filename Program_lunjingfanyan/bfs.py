#!/usr/bin/python
# -*- coding: UTF-8 -*-

#graph ={'A':['B','C','E'],'B':['A','D','E'],'C':['A','F','G'],'D':['B'],'E':['A','B','D'],'F':['C'],'G':['C']}

graph = {"1": ["2","3","4"], "2": ["1","3","5"], "3": ["1","2","4","5","6"], "4": ["1","3","6","7"], "5": ["2","3","6"], "6":["3","4","5","7"],"7":["4","6"]}

# visits all the nodes of a graph (connected component) using BFS

def bfs(graph, start, goal):
	# keep track of all visited nodes
	explored = []
	# keep track of nodes to be checked
	queue = [[start]]
	# return path if start is goal 
	if start == goal:
		return "That was easy! Start = goal"
	while queue:
		# pop shallowest node (first node) from queue
		path = queue.pop(0)	# path is a list stored the path
		# get the last node from the path
		node = path [-1]		# 注意node代表dict 的key，所以value 和key是一个类型的 
		if node not in explored:
					
			neighbours = graph[node]	# neighbours 是一个相邻节点的列表. 要考虑一个节点不存在的情况么？
 			# go through all eighbour nodes, construct a new path
			# push it into the queue
			# add node to list of checked nodes
			#explored.append(node)
			#neighbours = graph[node]
			# add neighbours of node to queue
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				if neighbour == goal:
					return new_path
			# mark node as explored
			explored.append(node)
	return ("So sorry, but a conncting path doesn't exist: "( bfs(graph, "G", "D")))
	
path = bfs(graph,"1","7")

print(path)