#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
"""


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def check_route1(self, start_node, end_node):
        """ use bfs algorithm """
        q = [start_node]  # queue
        visited = []
        while q:
            cur = q.pop(0)
            for i in self.gdict[cur]:
                q.append(i)
            if cur not in visited:
                visited.append(cur)
            if end_node in visited:
                return True
        return False

    def check_route2(self, start_node, end_node):
        """ use dfs algorithm """
        stack = [start_node]
        visited = []
        while stack:
            cur = stack.pop()
            for i in self.gdict[cur]:
                stack.append(i)
            if cur not in visited:
                visited.append(cur)
            if end_node in visited:
                return True
        return False


if __name__ == '__main__':
    customDict = {"a": ["c", "d", "b"],
                  "b": ["j"],
                  "c": ["g"],
                  "d": [],
                  "e": ["f", "a"],
                  "f": ["i"],
                  "g": ["d", "h"],
                  "h": [],
                  "i": [],
                  "j": []
                  }

    g = Graph(customDict)
    assert g.check_route1("a", "j")
    assert g.check_route2("a", "j")
    assert g.check_route1("e", "i")
    assert g.check_route2("e", "i")
    assert not g.check_route1("a", "i")
    assert not g.check_route2("a", "i")
    assert not g.check_route1("h", "f")
    assert not g.check_route2("h", "f")
