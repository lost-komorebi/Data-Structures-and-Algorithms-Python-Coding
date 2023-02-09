#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        if not self.list:
            return True
        return False


def html_checker(html: str) -> bool:
    html = html.split()
    tag_stack = Stack()
    has_tag_appear = False  # there is at least one tag appear in the whole string
    for i in html:
        if i[0] == '<' and i[-1] == '>' and i[1] != '/':  # open tag
            has_tag_appear = True
            tag_stack.push(i)
        if i[:2] == '</' and i[-1] == '>':  # close tag
            if tag_stack.is_empty():  # close tag appear before open tag or extra open tag
                return False
            pop_string = tag_stack.pop()
            if pop_string[1:-1] != i[2:-1]:
                return False
    if not tag_stack.is_empty():  # open tag and close tag must appear in pairs
        return False
    return has_tag_appear


if __name__ == '__main__':
    html_str = """<html>
     <head>
        <title>
          Example
        </title>
     </head>
     <body>
        <h1>Hello, world</h1>
     </body>
   </html>"""
    assert html_checker(html_str)
