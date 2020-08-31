# -*- coding: UTF-8 -*- 

'''
采用BFS广度优先算法找到最短路径，暂未考虑线路出现回路的情况

'''
# 首先定义线路结构图

graph = {"1": ["2","3","4"], "2": ["1","3","5"], "3": ["1","2","4","5","6"], "4": ["1","3","6","7"], "5": ["2","3","6"], "6":["3","4","5","7"],"7":["4","6"]}


# 下面是输出线路的结构图，分别打印每个节点的

'''
print("线路的连接图是：")
for i in graph.keys():
    print("graph[%s]: %s" %(i, graph[i]))
'''

# bfs 实现    
def bsf(graph, start , end):
    
    checked = []        #储存已经检查过的节点
    
    queue = [[start]]   # 将含有起始节点的列表存入队列中
    
    
    if start == end:
        return "输入的起始节点：【%s】与末尾节点：【%s】一致，请检查节点输入是否正确。"%(start, end)
    
    while queue:                # 如果队列中有节点
        path = queue.pop(0)     #将队列中的第一个路径列表取出
        node = path[-1]
        #初始化完成
        
        if node not in checked:
            #print("Current node is : ", node )
            neighbours = graph[node]
            #print("graph[%s]:%s"%(node, neighbours))
            for neighbour in neighbours:
                #print("path:",path)
                new_path =list(path)   ##大坑，加list后代表path和new_path在不同的地址上
                #print(id(path),id(new_path))
                #print("new_path:",new_path)
                new_path.append(neighbour)
                #print("new_path.append: ", new_path)
                queue.append(new_path)      
                #print("queue: ", queue)
                if neighbour == end:
                    return new_path
                                    
            #print("检查完一个节点了,我们进入下一个节点")
            checked.append(node)
    
    
    return ("没有找到起点：【%s】 到 终点：【%s】 的路径，请检查节点是否正确" %(start, end))
        

path = bsf(graph, "2", "7")
print("最短路径为：\n", path)
