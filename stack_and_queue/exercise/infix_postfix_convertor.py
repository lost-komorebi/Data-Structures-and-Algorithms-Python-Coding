#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" convert an infix expression to postfix expression """


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        s = self.items.pop()
        return s

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]


def infix_to_postfix(expression: str) -> str:
    expression = expression.split(' ')
    operands = [chr(i).upper() for i in range(97, 97 + 26)]
    # store precedence level for operators
    pre = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 2, '(': 0}
    op_stack = Stack()
    output_list = []
    for i in expression:
        # If the token is an operand, append it to the end of the output list.
        if i in operands or i.isdigit():
            output_list.append(i)
        # If the token is a left parenthesis, push it on the op_stack.
        elif i == '(':
            op_stack.push(i)
        # If the token is a right parenthesis, pop the op_stack until the corresponding left parenthesis is removed.
        # Append each operator to the end of the output list.
        elif i == ')':
            pop_string = op_stack.pop()
            while pop_string != '(':
                output_list.append(pop_string)
                pop_string = op_stack.pop()
        # If the token is an operator, *, /, +, or −, push it on the op_stack. However,
        # first remove any operators already on the op_stack that have higher or equal precedence
        # and append them to the output list.
        else:
            if not op_stack.is_empty() and pre[op_stack.peek()] >= pre[i]:
                output_list.append(op_stack.pop())
            op_stack.push(i)
    while not op_stack.is_empty():
        output_list.append(op_stack.pop())
    return ' '.join(output_list)


def calculate_postfix(expression: str) -> float:
    expression = expression.split(' ')
    digits = '0123456789'
    op_stack = Stack()
    for i in expression:
        if i in digits:
            op_stack.push(i)
        else:
            operand1 = op_stack.pop()
            operand2 = op_stack.pop()
            # pay attention with the order of two operands
            result = eval(operand2 + i + operand1)
            op_stack.push(str(result))
    return op_stack.pop()


if __name__ == '__main__':
    print(infix_to_postfix('A * B + C * D'))
    print(infix_to_postfix('A + B * C'))
    print(infix_to_postfix('( A + B ) * ( C + D )'))
    print(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'))
    print(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'))
    print(calculate_postfix('4 5 6 * +'))
    print(calculate_postfix('7 8 + 3 2 + /'))
