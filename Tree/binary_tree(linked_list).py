#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from stack_and_queue.queue_by_linked_list import Queue
import sys
sys.path.append('..')


class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    queue = Queue()
    queue.en_queue(root_node)
    while not queue.is_empty():
        root = queue.de_queue()
        print(root.data)
        if root.left_child is not None:
            queue.en_queue(root.left_child)
        if root.right_child is not None:
            queue.en_queue(root.right_child)


def search(root_node, target_node_data):
    if not root_node:
        raise Exception('The binary tree does not exist.')
    queue = Queue()
    queue.en_queue(root_node)
    while not queue.is_empty():
        root = queue.de_queue()
        if root.data == target_node_data:
            return root.data
        if root.left_child is not None:
            queue.en_queue(root.left_child)
        if root.right_child is not None:
            queue.en_queue(root.right_child)
    return None


def insert(root_node, target_node):
    if not root_node:
        root_node.data = target_node.data
    else:
        queue = Queue()
        queue.en_queue(root_node)
        while not queue.is_empty():
            root = queue.de_queue()
            if root.data == target_node:
                return root.data
            if root.left_child is not None:
                queue.en_queue(root.left_child)
            else:
                root.left_child = target_node
                return
            if root.right_child is not None:
                queue.en_queue(root.right_child)
            else:
                root.right_child = target_node
                return


def get_deepest_node(root_node):
    if not root_node:
        return
    queue = Queue()
    queue.en_queue(root_node)
    root = None
    while not queue.is_empty():
        root = queue.de_queue()
        if root.left_child is not None:
            queue.en_queue(root.left_child)
        if root.right_child is not None:
            queue.en_queue(root.right_child)
    return root


def delete(root_node, node_to_delete):
    if not root_node:
        return
    deepest_node = get_deepest_node(root_node)
    queue = Queue()
    queue.en_queue(root_node)
    while not queue.is_empty():
        root = queue.de_queue()
        if root is node_to_delete:
            node_to_delete.data = deepest_node.data
            deepest_node.data = None
            return
        else:
            if root.left_child is not None:
                queue.en_queue(root.left_child)
            if root.right_child is not None:
                queue.en_queue(root.right_child)


def clear(rootNode):
    """ delete entire binary tree """
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None


if __name__ == '__main__':
    my_tree = TreeNode('menu')
    food = TreeNode('food')
    drink = TreeNode('drink')
    rice = TreeNode('rice')
    noodle = TreeNode('noodle')
    beer = TreeNode('beer')
    cola = TreeNode('cola')
    my_tree.left_child = food
    my_tree.right_child = drink
    food.left_child = rice
    food.right_child = noodle
    drink.left_child = beer
    drink.right_child = cola
    # print(pre_order_traversal(root), '\n')
    # print(in_order_traversal(root), '\n')
    # print(post_order_traversal(root), '\n')
    # print(level_order_traversal(root), '\n')
    # print(search(root_node, 'cola1'), '\n')
    ice_cream = TreeNode('ice cream')
    cup_cake = TreeNode('cup cake')
    insert(my_tree, cup_cake)
    insert(my_tree, ice_cream)
    # print(level_order_traversal(root))
    # print(food.left_child.data, food.right_child.data)
    # print(get_deepest_node(root).data)
    print(delete(my_tree, food))
    print(level_order_traversal(my_tree))
    # print(get_deepest_node(my_tree).data)
