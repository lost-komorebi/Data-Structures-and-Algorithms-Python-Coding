#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   topological_sorting.py
@Time    :   2023/04/06 15:15:20
@Author  :   komorebi 
'''
"""
1. Call dfs(g) for some graph g. 
   The main reason we want to call depth first search is to compute the finish times for each of the vertices.
2. Store the vertices in a list in decreasing order of finish time.
3. Return the ordered list as the result of the topological sort.
"""

from general_dfs import DfsGraph

def topological(g: DfsGraph):
    g.dfs()
    return sorted(g.vertices, key=lambda x:g.vertices[x].finish_time, reverse=True)

if __name__ == '__main__':
    g = DfsGraph()
    g.add_edge('3/4 cup milk', '1 cup mix')
    g.add_edge('1 egg', '1 cup mix')
    g.add_edge('1 Tbl Oil', '1 cup mix')
    g.add_edge('1 cup mix', 'heat syrup')
    g.add_edge('1 cup mix', 'pour 1/4 cup')
    g.add_edge('heat griddle', 'pour 1/4 cup')
    g.add_edge('pour 1/4 cup', 'turn when bubbly')
    g.add_edge('heat syrup', 'eat')
    g.add_edge('turn when bubbly', 'eat')
    print(topological(g))