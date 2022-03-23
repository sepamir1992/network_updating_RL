import pandas as pd
from collections import OrderedDict
import collections
import json
from collections import defaultdict
import networkx as nx

#from sys import setrecursionlimit
#setrecursionlimit(1000000)
#threading.stack_size(2**27)  # new thread will get stack of such size


#67199
#13439998

#df_firstn = pd.read_csv("D:\CSC 579\Project\PT\pt1.csv")

mylist = []
Pts = []
list2 = []
CurrentPt = []


# Python program to detect cycle
# in a graph



# =============================================================================
# class Graph():
# 	def __init__(self,vertices):
# 		self.graph = defaultdict(list)
# 		self.V = vertices
# 
# 	def addEdge(self,u,v):
# 		self.graph[u].append(v)
# 
# 	def isCyclicUtil(self, v, visited, recStack):
# 
# 		# Mark current node as visited and
# 		# adds to recursion stack
# 		visited[v] = True
# 		recStack[v] = True
# 
# 		# Recur for all neighbours
# 		# if any neighbour is visited and in
# 		# recStack then graph is cyclic
# 		for neighbour in self.graph[v]:
# 			if visited[neighbour] == False:
# 				if self.isCyclicUtil(neighbour, visited, recStack) == True:
# 					return True
# 			elif recStack[neighbour] == True:
# 				return True
# 
# 		# The node needs to be poped from
# 		# recursion stack before function ends
# 		recStack[v] = False
# 		return False
# 
# 	# Returns true if graph is cyclic else false
# 	def isCyclic(self):
# 		visited = [False] * (self.V + 1)
# 		recStack = [False] * (self.V + 1)
# 		for node in range(self.V):
# 			if visited[node] == False:
# 				if self.isCyclicUtil(node,visited,recStack) == True:
# 					return True
# 		return False
# =============================================================================




# Thanks to Divyanshu Mehta for contributing this code


def construct_trees_by_TingYu(edges):
    """Given a list of edges [child, parent], return trees. """
    trees = collections.defaultdict(dict)
    for child, parent in edges:
        trees[parent][child] = trees[child]
    # Find roots
    children, parents = zip(*edges)
    roots = set(parents).difference(children)
    return {root: trees[root] for root in roots}


def list_words(trie):
    my_list = []
    for k,v in trie.items():
        if len(v) != 0:
            for el in list_words(v):
                my_list.append(str(k)+', ' + str(el))
        else:
            my_list.append('')
    return my_list




#https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/reconstruct-itinerary.py
def findItinerary(origin, flows, flow_id, file):

        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def route_helper(origin, flow_cnt, graph, ans):
            if flow_cnt == 0:
                return True

            for i, (dest, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    ans.append(dest)
                    if route_helper(dest, flow_cnt - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

        graph = collections.defaultdict(list)
        for flow in flows:
            graph[flow[0]].append([flow[1], True])
        for k in graph.keys():
            graph[k].sort()

        ans = [origin]
        route_helper(origin, len(flows), graph, ans)
        #print('flow ' + str(flow_id) +':', ans)
        CurrentPt.append(ans)
        file.write(str(ans))
        file.write("\n")
        return ans

# =============================================================================
# 
#print((df_firstn.loc[df_firstn['flow_id'] == 0].iloc[0]))
# 
# print(((df_firstn.loc[df_firstn['flow_id'] == 0])).shape[0])
# =============================================================================

def check_for_loop(flows):
    nodes = set()
    
    DG = nx.DiGraph()    
    
    for x in range(len(flows)):
            DG.add_edge(flows[x][0], flows[x][1])
            
    #nx.draw(DG, with_labels=True, font_weight='bold')
    
    def check_attribute(DG, node):
        # Say the condition is node id is 3:
        return node == 3

    #g = Graph(len(nodes))
    
    #for flow in flows:
        #g.addEdge(flow[0], flow[1])
    
    if len(nx.recursive_simple_cycles(DG)) >0:
        return False
    elif len(nx.recursive_simple_cycles(DG)) ==0:
        return True
    #return not g.isCyclic()

 

def makelist(i): 
    split_flow=[]
    path = {}
    final_list = []
    
    my_list = []
    df_firstn = pd.read_csv("D:/CSC 579/Project/PT (2)/pt"+str(i)+".csv")
    file = open("D:\CSC 579\Project\PT (2)\Pt_texts\pt"+str(i)+".txt", "w")

    for flow_id in range(0, 600):
        flows = []
    
    
        #print('flow: ' + str(i))
        for k in range (((df_firstn.loc[df_firstn['flow_id'] == flow_id])).shape[0]):
    
            if (df_firstn.loc[df_firstn['flow_id'] == flow_id].iloc[k])['ratio'] > 0:

                flows.append([(df_firstn.loc[df_firstn['flow_id'] == flow_id].iloc[k])['from_node'],
                      (df_firstn.loc[df_firstn['flow_id'] == flow_id].iloc[k])['to_node']])
            
            ####CHECK WHERE THE FLOW SPLITS######
            if 0<((df_firstn.loc[df_firstn['flow_id'] == flow_id].iloc[k])['ratio']) <1:
                split_flow.append(flow_id)
        
    # =============================================================================
    
        if check_for_loop(flows):

            #The path is a nested dictionary
            path = construct_trees_by_TingYu(flows)
            origin = int(flow_id/24)
    
            my_list = list_words(path)

        
            test_list = [k.split(',') for k in my_list]
            
            if len(test_list) != 0:
                for i in range (len(test_list)):
                    test_list[i].append(str(origin))
                    pre_list = []
                
                    for j in range (len(test_list[i])):
    
                        if test_list[i][j].strip():
                            pre_list.append(int(test_list[i][j]))
                    #bring the origin to the begining of each list
                    pre_list.reverse()
                    final_list.append(pre_list)
                    file.write(str(pre_list))
                    file.write("\n")
            
                #print('flow ' + str(flow_id) +':', final_list)
                final_list=[]
                CurrentPt.append(final_list)

    file.close()
    return CurrentPt
    

    
    
        
# =============================================================================
   
      
for i in range(1, 2):
    CurrentPt = []
    makelist(i) 
# =============================================================================
#     if i == 0:
#         Pt0 = CurrentPt
#     if i == 1:
#         pt1 = CurrentPt
# =============================================================================
    
# =============================================================================
# newlist = [item for item in Pt0 if item not in pt1]
# print (newlist)
# =============================================================================

            
            
            
            

 
    


        
        
       
















            # if((df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['ratio'] >= 0.5):
              #    if((df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['flow_id']==0 ):
                 
        
            #mylist.append([(df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['from_node'],
                     #(df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['to_node'],
                     #(df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['ratio']])
                  #   mylist.append([(df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['from_node'],
                        #   (df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['to_node']])
            
            
# =============================================================================
#              elif((df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['flow_id']==0 ):
#                  if((df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['ratio'] >= 0.5):
#                  
#                     print((df_firstn.loc[df_firstn['from_node'] == i].iloc[k])['flow_id'])
# =============================================================================
                



        
