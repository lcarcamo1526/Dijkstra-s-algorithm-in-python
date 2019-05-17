#!/usr/bin/env python
# coding: utf-8

# ## IMPORTING LIBRARIES

# In[6]:


import matplotlib.pyplot as plt


# In[37]:


#init graph

#mutable and unordered
def initial_graph() :
        return {   
            'A': {'B':1, 'C':4, 'D':2},
            'B': {'A':9, 'E':5},
            'C': {'A':4, 'F':15},
            'D': {'A':10, 'F':7},
            'E': {'B':3, 'J':7},
            'F': {'C':11, 'D':14, 'K':3, 'G':9},
            'G': {'F':12, 'I':4},
            'H': {'J':13},
            'I': {'G':6, 'J':7},
            'J': {'H':2, 'I':4},
            'K': {'F':6} 
        }
   
   


# In[18]:


#init variables
graph = initial_graph()


# ## VISUALIZE DATA

# <img src = "https://i.postimg.cc/FKfFdfp2/grafo1.png" align = "center">

# In[33]:


# Grapviz https://graphviz.org/


# In[82]:


def Shortest_path(graph,initial,final):
    #shortest path
    path = {}
    #neighbouring nodes
    adj_node = {}
    #Queue for manipulation
    
    queue = []
    #Check all nodes and initialize path with 0
    for node in graph:
        path[node] = float("inf")
        adj_node[node] = None
        queue.append(node)

    path[initial] = 0
    #Check visited nodes and also to find the minimum distance between the nodes.
    while queue:
        key_min = queue[0]
        min_val = path[key_min]
        for n in range(1, len(queue)):
            if path[queue[n]] < min_val:
                key_min = queue[n]
                min_val = path[key_min]
        cur = key_min
        queue.remove(cur)
        #rint(cur)

        for i in graph[cur]:
            alternate = graph[cur][i] + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                
                adj_node[i] = cur
                

    #Finally, print nodes that satisfies the condition
    print('Shortest route between {} to {}'.format(initial,final))
    print(final, end='<-')
    while True:
        final = adj_node[final]
        if final is None:
            
            print("")
            break
        print(final, end='<-')
       
     


# In[83]:


Shortest_path(graph,'A','H')


# In[ ]:




