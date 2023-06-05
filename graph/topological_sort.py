#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
only suitable for sorting directed acyclic graph to a linear
"""
from stack_and_queue.queue_by_linked_list import Queue
import sys
sys.path.append('..')


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def add_neighbors(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()


class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.graph:
            self.graph[vertex.name] = vertex
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        """ directed graph, only add vertex2 as neighbors of vertex1 """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].add_neighbors(vertex2)
            return True
        return False

    def print_graph(self):
        for key in sorted(list(self.graph.keys())):
            print(key, str(self.graph[key].neighbors))

    def topological_sort(self):
        """
        1.Identify the node that has no in-degree(no incoming edges) and select that node as the source node of the graph
        2.Delete the source node with zero in-degree and also delete all its outgoing edges from the graph.
        Insert the deleted vertex in the result array.
        3.Update the in-degree of the adjacent nodes after deleting the outgoing edges
        4.Repeat step 1 to step 3 until the graph is empty
        """
        # calculate in_degrees
        result = []  # store topological sorting result
        in_degrees = {}
        for key in self.graph:
            in_degrees[key] = 0  # init count for each vertex
            for value in self.graph.values():
                if key in value.neighbors:
                    in_degrees[key] += 1
        # init queue
        q = Queue()
        for vertex in in_degrees:
            if in_degrees[vertex] == 0:
                q.en_queue(vertex)
        while not q.is_empty():
            cur = q.de_queue()
            result.append(cur)
            # update in_degree
            for vertex in self.graph[cur].neighbors:
                in_degrees[vertex] -= 1
                if in_degrees[vertex] == 0:
                    q.en_queue(vertex)
        print(result)

    def topological_sort1(self):
        """ recursion """
        visited = []  # mark all vertices as not visited
        stack = []
        for vertex in self.graph:  # loop all vertices
            if vertex not in visited:
                self.helper(vertex, visited, stack)

        print(stack)

    def helper(self, vertex, visited, stack):
        visited.append(vertex)  # mark current vertex as visited

        # recur all neighbors of current vertex
        for i in self.graph[vertex].neighbors:
            if i not in visited:
                self.helper(i, visited, stack)

        stack.insert(0, vertex)


if __name__ == '__main__':
    my_graph = Graph()
    for i in range(ord('a'), ord('h') + 1):
        my_graph.add_vertex(Vertex(chr(i)))
    edges = ['ac', 'bc', 'bd', 'ce', 'df', 'eh', 'ef', 'fg']
    for i in edges:
        my_graph.add_edge(i[0], i[-1])
    my_graph.print_graph()
    print(my_graph.topological_sort())
    print(my_graph.topological_sort1())

    my_graph1 = Graph()
    for i in range(0, 6):
        my_graph1.add_vertex(Vertex(str(i)))
    edges = ['52', '50', '41', '23', '40', '31']
    for i in edges:
        my_graph1.add_edge(i[0], i[-1])
    my_graph1.print_graph()
    print(my_graph1.topological_sort())
    print(my_graph1.topological_sort1())
