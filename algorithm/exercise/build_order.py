#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.
use topological sort
"""


def create_graph(projects, dependencies):
    project_graph = {}
    for project in projects:
        project_graph[project] = []
    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])
    return project_graph


def find_build_order(projects, dependencies):
    graph = create_graph(projects, dependencies)
    # calculate indegree
    indegree_map = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree_map[neighbor] += 1
    non_indegree_nodes = []  # stack fifo
    # find nodes which indegree is 0
    for node in indegree_map:
        if indegree_map[node] == 0:
            non_indegree_nodes.append(node)
    topological_path = []
    while non_indegree_nodes:
        node = non_indegree_nodes.pop()
        topological_path.append(node)
        #  node is visited, so reduce indegree of node's neighbors
        for i in graph[node]:
            indegree_map[i] -= 1
            if indegree_map[i] == 0:
                non_indegree_nodes.append(i)
    # check if all nodes in topological_path
    if len(topological_path) == len(graph.keys()):
        return topological_path
    else:
        print('no topological path for current graph')


if __name__ == '__main__':
    project = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    find_build_order(project, dependencies)
