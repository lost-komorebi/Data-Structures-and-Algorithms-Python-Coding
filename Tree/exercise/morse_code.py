#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@File    :   morse_code.py
@Time    :   2023/05/06 13:36:01
@Author  :   komorebi 
'''
""" morse code implementation by using python tree data structure """


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def replace(self, data, parent, left, right):
        """ replace content of a node with new values """
        self.data = data
        if parent.left == self:
            parent.left = self
            self.left = left
            self.right = right
        else:
            parent.right = self
            self.left = left
            self.right = right



class MorseCodeTree(Node):

    def __init__(self) -> None:
        self.root = Node('start')

    def insert(self, data, code):
        prev = None
        cur = self.root
        for i in code:
            prev = cur
            if i == '.':
                cur = cur.left
                if not cur: # use placeholder for next iteration
                    cur = Node('empty')
                    prev.left = cur
            else:
                cur = cur.right
                if not cur: # use placeholder for next iteration
                    cur = Node('empty')
                    prev.right = cur
        # we have arrived the corresponding postion
        if cur is None or cur.data == 'empty':
            if i == '.':
                cur.replace(data, prev, cur.left, cur.right)
            else:
                cur.replace(data, prev, cur.left, cur.right)


    def has_path(self, root, letter, path):
        """ use preorder to find if there is a path from root """
        if not root:
            return False
        elif root.data == letter:
            return True
        else:
            if self.has_path(root.left, letter, path) == True:
                path.insert(0, '.')
                return True
            elif self.has_path(root.right, letter, path) == True:
                path.insert(0, '-')
                return True

    def encode(self, text):
        morse_code = ''
        for chr in text:
            path = []
            success = self.has_path(self.root, chr, path)
            if not success:
                raise ValueError(f'No morse code for {chr}')
            morse_code = morse_code + ' ' + ''.join(path) 
        return morse_code

    def decode(self, text):
        """ convert morse code to human readable text """
        temp = []
        for i in text.split(' '):
            cur = self.root
            for j in i:
                if j == '.':
                    cur = cur.left
                else:
                    cur = cur.right
            temp.append(cur.data)
        return ''.join(temp)
        
def pretty_print_tree(root):
    """
    This function pretty prints a binary tree
    :param root: root of tree
    :return: none
    """
    lines, _, _, _ = _pretty_print_tree(root)
    for line in lines:
        print(line)

def _pretty_print_tree(root):
    """
    Code credits: Stack overflow
    :param root: root of tree
    :return: none
    """
    if root.right is None and root.left is None:
        line = '%s' % root.data
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = _pretty_print_tree(root.left)
        s = '%s' % root.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = _pretty_print_tree(root.right)
        s = '%s' % root.data
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _pretty_print_tree(root.left)
    right, m, q, y = _pretty_print_tree(root.right)
    s = '%s' % root.data
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

if __name__ == '__main__':

    
    morse_code_tree = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    
    my_mct = MorseCodeTree()
    print(my_mct.root.data)
    for i in morse_code_tree:
        my_mct.insert(i, morse_code_tree[i])    
    pretty_print_tree(my_mct.root)
    
    print(my_mct.decode('.- -... -.-.'))
    
    print(my_mct.encode('ABC'))