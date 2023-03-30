#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :    general_dfs.py
@Time    :   2023/03/30 20:01:20
@Author  :   komorebi 
'''

""" general depth first search """




from graph import Vertex, Graph
class DfsGraph(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:  # iterate all vertices
            if not vertex.get_color():
                self.dfs_helper(vertex)

    def dfs_helper(self, vertex):
        print(f'current vertex {vertex.get_name()}')
        vertex.set_color('gray')
        self.time += 1
        vertex.set_discovery_time(self.time)
        for nbr in vertex.get_connections():
            if not nbr.get_color():  # nbr is not visited
                nbr.set_prev(vertex)
                self.dfs_helper(nbr)
        print(f'current vertex {vertex.get_name()}')
        self.time += 1
        print(f'set vertex {vertex.get_name()} to black')
        # set a vertex to black when this vertex has no neighbor to explore
        vertex.set_color('black')
        vertex.set_finish_time(self.time)


if __name__ == '__main__':
    g = DfsGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'D')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'B')
    g.add_edge('E', 'F')
    g.add_edge('F', 'C')
    g.dfs()
    for vertex in g:
        print(vertex, vertex.discovery_time,
              vertex.finish_time, vertex.get_color())
