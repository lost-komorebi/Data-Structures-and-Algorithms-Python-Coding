#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" using dict to represent graph """
from stack_and_queue.queue_by_linked_list import Queue
from stack_and_queue.stack_by_linked_list import StackByLinkedList
import sys
import random
sys.path.append('..')


class Graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            self.g_dict = {}
        else:
            self.g_dict = g_dict

    def __repr__(self):
        result = ''
        for i in self.g_dict:
            result += str(i) + ': ' + str(self.g_dict[i]) + '\n'
        return result

    def add_vertex(self, vertex):
        if vertex not in self.g_dict.keys():
            self.g_dict[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.g_dict.keys() and vertex2 in self.g_dict.keys():
            if vertex2 not in self.g_dict[vertex1]:
                self.g_dict[vertex1].append(vertex2)
            if vertex1 not in self.g_dict[vertex2]:
                self.g_dict[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.g_dict.keys() and vertex2 in self.g_dict.keys():
            try:
                self.g_dict[vertex1].remove(vertex2)
                self.g_dict[vertex2].remove(vertex1)
            except ValueError:
                raise Exception(f'no edges between {vertex1} and {vertex2}')
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex not in self.g_dict.keys():
            raise Exception(f'no vertex named {vertex}')
        for i in self.g_dict:
            if vertex in self.g_dict[i]:
                self.remove_edge(i, vertex)
        del self.g_dict[vertex]

    def bfs_traversal(self, start):
        """ breadth first traversal """
        queue = Queue()
        queue.en_queue(start)
        visited_vertex = [start]
        print("start bfs traversal")
        while not queue.is_empty():  # queue is not empty
            p = queue.de_queue()
            print(p)
            for i in self.g_dict[p]:
                if i not in visited_vertex:
                    queue.en_queue(i)
                    visited_vertex.append(i)

    def dfs_traversal(self, start):
        """ depth first traversal """
        stack = StackByLinkedList()
        stack.push(start)
        visited_vertex = [start]
        print('start dfs traversal')
        while not stack.is_empty():
            p = stack.pop()
            print(p)
            for i in self.g_dict[p]:
                if i not in visited_vertex:
                    stack.push(i)
                    visited_vertex.append(i)


if __name__ == '__main__':
    my_graph = Graph()
    print(my_graph.g_dict)
    my_graph.add_vertex('a')
    my_graph.add_vertex('b')
    my_graph.add_vertex('c')
    my_graph.add_vertex('d')
    my_graph.add_vertex('e')
    my_graph.add_vertex('f')
    my_graph.add_vertex('g')
    my_graph.add_edge('a', 'b')
    my_graph.add_edge('a', 'c')
    my_graph.add_edge('b', 'd')
    my_graph.add_edge('b', 'g')
    my_graph.add_edge('c', 'd')
    my_graph.add_edge('c', 'e')
    my_graph.add_edge('d', 'b')
    my_graph.add_edge('d', 'f')
    my_graph.add_edge('e', 'c')
    my_graph.add_edge('e', 'f')
    my_graph.add_edge('f', 'd')
    my_graph.add_edge('f', 'e')
    my_graph.add_edge('f', 'g')
    my_graph.add_edge('g', 'b')
    my_graph.add_edge('g', 'f')
    print(my_graph)
    print(my_graph.bfs_traversal('a'))
    print(my_graph.dfs_traversal('a'))
