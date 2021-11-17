# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:42:06 2021

@author: Josh Hicks
"""

import random
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

G.clear()

edges = [[4,1], [4,2], [4,12], [1, 3] ,[2,1] , [3, 2], [3,5], [5,6], [5,8], [6,7],[6,8], [7,10], [8,9], [8,10], [9,5], [9,11],[10,9], [10,11], [11,12]]

#print("These are the edges: " , edges)

#Adds the edges to g
G.add_edges_from(edges)

print("Plotting the Digraph")
# Draw the digraph to the screen
plt.figure(1)
nx.draw(G, with_labels= True)
plt.show()

#Finds the strongly connected nodes in the graph
strong = list(nx.strongly_connected_components(G))


#Convert the Digraph to a meta graph of its strongly connected parts
B = nx.DiGraph()
for b in range(len(strong)):
    for e in range(len(strong)):
        if b != e:
            for c in strong[b]:                
                if (any(i in G.neighbors(c) for i in strong[e])):
                    #print(",".join(strong[b]))
                    B.add_edge(",".join( str(elem) for elem in strong[b]), ",".join( str(elem) for elem in strong[e]))
                    break



    
#Draw the meta graph to the screen
print("Plotting the Meta Graph")
plt.figure(2)
nx.draw(B, with_labels=True, font_weight='bold')
plt.show()


top = list(nx.topological_sort(B))

positions = {}

for i in range(len(top)):
    positions[top[i]] = [i,pow(-1, i)]
    
print("Linearized as Dag")
plt.figure(3)
nx.draw(B, with_labels=True, font_weight='bold', pos = positions)
plt.show()


for i in range(len(top)):
    positions[top[i]] = [i,0]
print("Actually Linear")
plt.figure(4)
nx.draw(B, with_labels=True, font_weight='bold', pos = positions)
plt.show()
