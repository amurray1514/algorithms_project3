# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:44:47 2021

@author: Levi Lewis
"""

def dfs(graph, start, visited=None):

    # Initialization with empty set
    if visited is None:
        visited = set() 

    # Mark start visited and add it to visited
    visited.add(start)

    # For key in adjancency list set of start but
    # not yet visited visit the key
 
    for key in graph[start] - visited: # Python suports set subtraction       
        dfs(graph, key, visited) # DFS recursive call
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

def bfs_path(graph, start, goal):
    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0) 
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None 

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

# Sample graph
graph = {'A': set(['B', 'F', 'E']),
         'B': set(['A', 'C', 'F']),
         'C': set(['B', 'D', 'G']),
         'D': set(['C', 'G']),
         'E': set(['A', 'F', 'I']),
         'F': set(['A', 'B', 'E', 'I']),
         'G': set(['C', 'D', 'J']),
         'H': set(['K', 'L']),
         'I': set(['E', 'F', 'J', 'M']), 
         'J': set(['I', 'G']), 
         'K': set(['H', 'L', 'O']), 
         'L': set(['H', 'K', 'P']),
         'M': set(['I', 'N']), 
         'N': set(['M']), 
         'O': set(['K']), 
         'P': set(['L'])}

# =============================================================================
# v = dfs(graph, 'A')
# u = dfs(graph, 'H')
# w = bfs(graph, "A")
# z = bfs(graph, "H")
# print(v)
# print(u)
# print(w)
# print(x)
# =============================================================================

# =============================================================================
# a = bfs_path(graph, "D", "N")
# b = dfs_path(graph, "D", "N")
# c = dfs_path(graph, "A", "B")
# d = bfs_path(graph, "A", "B")
# print(a)
# print(b)
# print(c)
# print(d)
# =============================================================================

s = dfs_path(graph, "A", "B")
t = dfs_path(graph, "A", "B")
x = bfs_path(graph, "A", "B")
y = bfs_path(graph, "A", "B")
print(s)
print(t)
print(x)
print(y)

