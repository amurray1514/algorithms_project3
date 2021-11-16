#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code for CSCI 3330 Algorithms, Project 3, Part 3.

@author: Archer Murray
"""

import networkx as nx

def printAdjacencyList(g):
    """
    Prints an adjacency list representation of g.
    """
    adjList = nx.to_dict_of_lists(g)
    for n in adjList.keys():
        print(n + ': ' + str(adjList[n]))

def shortestPathTree(g, start):
    """
    Applies Dijkstra's algorithm via a NetworkX library function to produce
    the shortest path tree for g with starting node start.
    """
    shortestPaths = nx.shortest_path(g, start, weight='weight')
    ret = nx.Graph()
    for path in shortestPaths.values():
        for i in range(1, len(path)):
            ret.add_edge(path[i - 1], path[i])
    return ret

def minimumSpanningTree(g):
    """
    Applies Kruskal's algorithm via a NetworkX library function to produce the
    minimum spanning tree for g.
    """
    return nx.minimum_spanning_tree(g, weight='weight')

def isIsomorphic(g1, g2):
    """
    Returns True if and only if g1 and g2 are isomorphic; that is, they have
    the same nodes and edges.
    This function uses the Weisfeiler Lehman graph hash via the NetworkX
    library to test for graph equality quickly. It is strongly guaranteed that
    two graphs that are not isomorphic will have different hashes.
    """
    return nx.weisfeiler_lehman_graph_hash(g1) == \
        nx.weisfeiler_lehman_graph_hash(g2)

if __name__ == '__main__':
    g = nx.Graph()
    e = [('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12), ('B', 'C', 35),
         ('B', 'F', 36), ('B', 'H', 34), ('C', 'D', 4), ('C', 'E', 65),
         ('C', 'F', 42), ('D', 'E', 33), ('D', 'I', 30), ('E', 'F', 18),
         ('E', 'G', 23), ('F', 'G', 39), ('F', 'H', 24), ('G', 'H', 25),
         ('G', 'I', 21), ('H', 'I', 19)]
    g.add_weighted_edges_from(e)
    print('Adjacency list representation of graph: ')
    printAdjacencyList(g)
    print()
    # Part (a)
    spt = shortestPathTree(g, 'A')
    print('Adjacency list representation of shortest path tree from A: ')
    printAdjacencyList(spt)
    print()
    # Part (b)
    mst = minimumSpanningTree(g)
    print('Adjacency list representation of minimum spanning tree: ')
    printAdjacencyList(mst)
    print()
    # Part (c)
    for n in g.nodes:
        print('Shortest path tree from ' + n + ': ', end='')
        if isIsomorphic(mst, shortestPathTree(g, n)):
            print('equal to MST')
        else:
            print('not equal to MST')
    print()
    # Part (d)
    print('Changed edge from B to C to have weight -35')
    g.edges['B', 'C']['weight'] = -35
    print('Adjacency list representation of shortest path tree from A: ')
    try:
        printAdjacencyList(shortestPathTree(g, 'A'))
    except Exception as e:
        print('An error occurred:', e)
    print()