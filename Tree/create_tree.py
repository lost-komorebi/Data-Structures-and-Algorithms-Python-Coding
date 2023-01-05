#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class TreeNode:
    def __init__(self, data, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    # def __repr__(self, level=0):
    #     ret = "\t" * level + repr(self.data) + "\n"
    #     for child in self.children:
    #         ret += child.__repr__(level + 1)
    #     return ret

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, tree_node):
        self.children.append(tree_node)


root = TreeNode('menu')
food = TreeNode('food')
drink = TreeNode('drink')
rice = TreeNode('rice')
noodle = TreeNode('noodle')
beer = TreeNode('beer')
cola = TreeNode('cola')
root.add_child(food)
root.add_child(drink)
food.add_child(rice)
food.add_child(noodle)
drink.add_child(beer)
drink.add_child(cola)
print(root)
