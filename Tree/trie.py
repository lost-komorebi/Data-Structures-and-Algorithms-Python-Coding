#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class TrieNode:
    def __init__(self):
        self.children = {}  # dic to store character and its children link
        self.is_end = False  # set default end marker


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string: str):
        current_node = self.root  # start from root_node
        for i in string:
            child_node = current_node.children.get(
                i)  # try to check if i in current_node
            if child_node is None:  # i is not in current_node
                child_node = TrieNode()  # new a child_node
                # add new child_node to current_node's children
                current_node.children.update({i: child_node})
            current_node = child_node  # continue next node
        current_node.is_end = True  # insertion finish, set end mark

    def search(self, string: str):
        current_node = self.root
        for i in string:
            child_node = current_node.children.get(i)
            if child_node is None:  # cannot find i in trie
                return False
            current_node = child_node
        if current_node.is_end:  # full string, not just prefix
            return True
        return False

    def print_trie(self, cur_node=None):
        """ print all words in current trie """
        if cur_node is None:
            cur_node = self.root
        result = []
        if cur_node.children:  # cur_node.children = {}
            for k, v in cur_node.children.items():
                if v.is_end:
                    result.append(str(k))
                for s in self.print_trie(v):
                    result.append(str(k) + s)
        return result

    def delete(self, string: str, index: int = 0, root: TrieNode = None):
        if not self.search(string):  # check if string exists in binary heap
            raise ValueError(f'{string} not in binary heap')
        if root is None:
            root = self.root
        if len(string) <= index:
            return True
        ch = string[index]
        cur_node = root.children.get(ch)
        if cur_node is None:
            return True
        can_node_be_deleted = False  # set default value of can be deleted as False

        # the node we want to delete is also prefix of some other words
        # we cannot delete it, continue to next node
        if len(cur_node.children) > 1:
            self.delete(string, index + 1, cur_node)

        # current_node is the last character of string that we want to delete
        if index == len(string) - 1:
            # the string we want to delete is prefix of some other words
            # we just need to modify the end marker
            # eg: we want to delete 'api' from trie 'api','apis'
            if len(cur_node.children) >= 1:
                cur_node.is_end = False
                return False
            else:
                root.children.pop(ch)
                return True

        if cur_node.is_end:
            self.delete(string, index + 1, cur_node)
            return False

        can_node_be_deleted = self.delete(string, index + 1, cur_node)
        if can_node_be_deleted:
            root.children.pop(ch)
            return True
        else:
            return False

    def delete1(self, str_to_del: str, cur_node: TrieNode = None) -> TrieNode:
        if cur_node is None:
            cur_node = self.root
        if len(str_to_del) == 1:
            final_node = cur_node.children.get(str_to_del)
            if not final_node:  # str_to_del is not exist in current trie, raise an error
                cur_node.children.pop(str_to_del)
            else:
                final_node.is_end = False
            return cur_node
        else:
            cur_str = str_to_del[0]
            cur_node.children[cur_str] = self.delete1(
                str_to_del[1:], cur_node.children[cur_str])
            if not cur_node.children[cur_str].children:
                if cur_node.children[cur_str].is_end:
                    return cur_node
                else:
                    cur_node.children.pop(cur_str)
            else:
                return cur_node


if __name__ == '__main__':
    my_trie = Trie()
    my_trie.insert('hello')
    my_trie.insert("apple")
    my_trie.insert("api")
    my_trie.insert("apis")
    my_trie.insert("ap")
    my_trie.insert("k")
    my_trie.insert("baby")
    my_trie.insert("angelababy")
    my_trie.insert("angela")
    my_trie.insert("happy")
    my_trie.insert("happiness")
    print(my_trie.search('k'))
    print(my_trie.print_trie())
    my_trie.delete('k')
    print(my_trie.search('k'))
    print(my_trie.print_trie())
