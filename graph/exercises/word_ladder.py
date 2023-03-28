#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   word_ladder.py
@Time    :   2023/03/26 16:15:26
@Author  :   komorebi 
'''
"""
In a word ladder puzzle you must make the change occur gradually by changing one letter at a time. 
At each step you must transform one word into another word, you are not allowed to transform a word into a non-word
"""




from graph import Graph
def build_grap(word_list):
    g = Graph()
    buckets = {}
    # create buckets of words that differ by only one letter
    for i in word_list:
        for j in range(len(i)):
            bucket = i[:j] + '_' + i[j+1:]
            if bucket in buckets:
                buckets[bucket].append(i)
            else:
                buckets[bucket] = [i]
    # create vertices and edges for words in the same bucket
    for bucket in buckets:
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


def bfs(g: Graph, start):
    """ breadth first search """
    start.set_distance(0)
    start.set_prev(None)
    q = []
    q.append(start)
    visited = [start]
    while q:
        vertex = q.pop(0)
        if vertex not in visited:
            visited.append(vertex)
        for i in vertex.get_connections():
            if i not in visited and i not in q:
                # distance increases with level
                i.set_distance(vertex.get_distance()+1)
                i.set_prev(vertex)  # set predecessor
                q.append(i)


def traversal(y):
    """ find the path from start to the end """
    x = y
    while x.get_prev():
        print(x.get_name())
        x = x.get_prev()
    print(x.get_name())


if __name__ == '__main__':
    words = ['fool', 'foul', 'foil', 'fail', 'fall', 'pall', 'poll',
             'pool', 'cool', 'pole', 'pope', 'pale', 'sale', 'page', 'sage']
    g = build_grap(words)
    start = g.get_vertex('fool')
    bfs(g, start)
    traversal(g.get_vertex('sage'))
