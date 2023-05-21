#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   strongly_connected_components.py
@Time    :   2023/04/06 18:32:24
@Author  :   komorebi 
'''
"""
1. call dfs for the graph g to compute the finish times for each vertex
2. compute transposed graph gt
3. call dfs for the graph gt, but in the main loop of dfs explore each vertex in descending order of finish times that were computed in step 1
4. each tree in step 3 is a strongly connected component
tree: an undirected connected acylic graph, meaning that there are no cycles in the graph
"""




from general_dfs import DfsGraph
def graph_transpose(g: DfsGraph):
    """ transpose the graph(i.e. reverse all the edges in the graph) """
    gt = DfsGraph()
    for v in g.vertices:
        nbrs = g.get_vertex(v).neighbors
        for nbr in nbrs:
            gt.add_edge(nbr.get_name(), v)
    return gt


def dfs_decreasing(gt, g: DfsGraph):
    decreasing_vertices = sorted(  # sort vertices by descending order of finish times
        g.vertices, key=lambda x: g.vertices[x].finish_time, reverse=True)
    for vertex_name in decreasing_vertices:
        if not gt.vertices[vertex_name].get_color():  # current vertex is not visited
            print(gt.vertices[vertex_name].name, end=' ')
            dfs_helper(gt, gt.vertices[vertex_name])
            print(" ")


def dfs_helper(g, vertex):
    vertex.set_color('gray')  # start visiting a vertex
    for nbr in vertex.get_connections():
        if not nbr.get_color():  # nbr is not visited
            print(nbr.name, end=' ')
            dfs_helper(g, nbr)
    # set a vertex to black when this vertex has no neighbor to explore
    vertex.set_color('black')


def scc(g):
    g.dfs()
    gt = graph_transpose(g)
    dfs_decreasing(gt, g)


if __name__ == '__main__':
    g = DfsGraph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('B', 'E')
    g.add_edge('D', 'B')
    g.add_edge('E', 'A')
    g.add_edge('E', 'D')
    g.add_edge('D', 'G')
    g.add_edge('G', 'E')
    g.add_edge('C', 'F')
    g.add_edge('F', 'H')
    g.add_edge('H', 'I')
    g.add_edge('I', 'F')

    scc(g)
