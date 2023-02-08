#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

""" convert an infix expression to postfix or prefix expression """

OPERANDS = [chr(i).upper() for i in range(97, 97 + 26)]


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

    # parentheses check
    if not parentheses_checker(expression, 1):
        raise Exception('Invalid expression')
    # operator numbers = operand number - 1
    if not operators_checker(expression):
        raise Exception('Invalid expression')
    if not expression_checker(expression):
        raise Exception('Invalid expression')
    # store precedence level for operators
    pre = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 2, '(': 0}
    op_stack = Stack()
    output_list = []
    for i in expression:
        # If the token is an operand, append it to the end of the output list.
        if i in OPERANDS or i.isdigit():
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


def parentheses_checker(expression, n: int) -> bool:
    """
    if n == 0, so the expected result is no parentheses in expression
    if n == 1, so the expected result is parentheses appear in pairs or no parentheses in expression
    """
    if n == 0:
        if '(' not in expression and ')' not in expression:
            return True
        return False
    else:
        stack = Stack()
        for i in expression:
            if i == '(':
                stack.push(i)
            if i == ')':
                stack.pop()
        return stack.is_empty()


def operators_checker(expression):
    """ operator number = operand number - 1 """
    operator_number = 0
    operand_number = 0
    for i in expression:
        if i in '+-*/^':
            operator_number += 1
        if i.isdigit() or i in OPERANDS:
            operand_number += 1
    return operator_number == operand_number - 1


def expression_checker(expression):
    """ the expression can only contains '+-*/^()', numbers and alphabet """
    for i in expression:
        if i not in '+-*/^() ' and not i.isalnum():
            return False
    return True


def infix_to_prefix(expression: str) -> str:

    # parentheses check
    if not parentheses_checker(expression, 1):
        raise Exception('Invalid expression')
    # operator numbers = operand number - 1
    if not operators_checker(expression):
        raise Exception('Invalid expression')
    if not expression_checker(expression):
        raise Exception('Invalid expression')

    expression = expression.split(' ')[::-1]  # reverse expression

    # store precedence level for operators
    pre = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 2, ')': 0}
    op_stack = Stack()
    output_list = []
    for i in expression:
        # If the token is an operand, append it to the end of the output list.
        if i in OPERANDS or i.isdigit():
            output_list.append(i)
        # If the token is a right parenthesis, push it on the op_stack.
        elif i == ')':
            op_stack.push(i)
        # If the token is a left parenthesis, pop the op_stack until the corresponding right parenthesis is removed.
        # Append each operator to the end of the output list.
        elif i == '(':
            pop_string = op_stack.pop()
            while pop_string != ')':
                output_list.append(pop_string)
                pop_string = op_stack.pop()
        else:  # i is operator
            if op_stack.is_empty():
                op_stack.push(i)
            elif op_stack.peek() == ')':
                op_stack.push(i)
            elif pre[i] >= pre[op_stack.peek()]:
                op_stack.push(i)
            else:
                while not op_stack.is_empty() or op_stack.peek(
                ) != ')' or pre[i] < pre[op_stack.peek()]:
                    op_stack.pop()
    while not op_stack.is_empty():
        output_list.append(op_stack.pop())
    return ' '.join(reversed(output_list))  # reverse again


def calculate_postfix(expression: str) -> float:
    expression = expression.split(' ')

    # no parentheses
    if not parentheses_checker(expression, 0):
        raise Exception('Invalid expression')
    # operator numbers = operand number - 1
    if not operators_checker(expression):
        raise Exception('Invalid expression')
    if not expression_checker(expression):
        raise Exception('Invalid expression')

    op_stack = Stack()
    for i in expression:
        if i.isdigit():
            op_stack.push(i)
        else:
            operand1 = op_stack.pop()
            operand2 = op_stack.pop()
            # pay attention with the order of two operands
            result = eval(operand2 + i + operand1)
            op_stack.push(str(result))
    return op_stack.pop()


def infix_evaluator(expression):
    """
    Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion
    and the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right
    and use two stacks, one for operators and one for operands, to perform the evaluation.
    """
    expression = expression.split(' ')
    operator_stack = Stack()
    operand_stack = Stack()
    pre = {'/': 2, '*': 2, '+': 1, '-': 1, '(': 0}  # precedence level
    for i in expression:
        if i in OPERANDS or i.isdigit():
            operand_stack.push(i)
        elif i == '(':
            operator_stack.push(i)
        elif i == ')':
            pop_string = operator_stack.pop()
            while pop_string != '(':
                operand1 = str(operand_stack.pop())
                operand2 = str(operand_stack.pop())
                operand_stack.push(eval(operand1 + pop_string + operand2))
                pop_string = operator_stack.pop()
        else:
            if not operator_stack.is_empty(
            ) and pre[operator_stack.peek()] >= pre[i]:
                pop_string = operator_stack.pop()
                operand1 = str(operand_stack.pop())
                operand2 = str(operand_stack.pop())
                operand_stack.push(eval(operand2 + pop_string + operand1))
            operator_stack.push(i)
    while not operator_stack.is_empty():
        pop_string = operator_stack.pop()
        operand1 = str(operand_stack.pop())
        operand2 = str(operand_stack.pop())
        operand_stack.push(eval(operand2 + pop_string + operand1))
    return operand_stack.pop()


if __name__ == '__main__':
    print(infix_to_postfix('A * B + C * D'))
    print(infix_to_postfix('A + B * C'))
    print(infix_to_postfix('( A + B ) * ( C + D )'))
    print(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'))
    print(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'))
    print(calculate_postfix('4 5 6 * +'))
    print(calculate_postfix('7 8 + 3 2 + /'))
    print(infix_to_postfix('( A + B ) * ( C + D ) * ( E + F )'))
    # full parentheses
    print(infix_to_postfix('( ( ( A + B ) * ( C + D ) ) * ( E + F ) )'))
    print(infix_to_postfix('A + ( ( B + C ) * ( D + E ) )'))
    # full parentheses
    print(infix_to_postfix('( A + ( ( B + C ) * ( D + E ) ) )'))
    print(infix_to_postfix('A * B * C * D + E + F'))
    # full parentheses
    print(infix_to_postfix('( ( ( ( ( A * B ) * C ) * D ) + E ) + F )'))
    print(calculate_postfix('2 3 * 4 +'))
    print(calculate_postfix('1 2 + 3 + 4 + 5 +'))
    print(calculate_postfix('1 2 3 4 5 * + * +'))
    print(infix_to_postfix('( 1 + ( 2 * ( 3 + ( 4 * 5 ) ) ) )'))
    print(infix_evaluator('( 1 + ( 2 * ( 3 + ( 4 * 5 ) ) ) )'))
    print(infix_to_prefix('( A + B )'))
    print(infix_to_prefix('( ( A + ( B * C ) ) + D )'))
    print(infix_evaluator('1 + 2 * 2 + 3'))
    print(infix_evaluator('1 + 2 * 2 + 3 / 1 * 2 + 1'))
    print(infix_evaluator('( 1 + 2 ) * ( 3 + 4 ) * ( 5 + 6 )'))
    # full parentheses
    print(infix_evaluator('( ( ( 1 + 2 ) * ( 3 + 4 ) ) * ( 5 + 6 ) )'))
    print(infix_evaluator('1 + ( ( 2 + 3 ) * ( 4 + 5 ) )'))
    # full parentheses
    print(infix_evaluator('( 1 + ( ( 2 + 3 ) * ( 4 + 5 ) ) )'))
    print(infix_evaluator('1 * 2 * 3 * 4 + 5 + 6'))
    # full parentheses
    print(infix_evaluator('( ( ( ( ( 1 * 2 ) * 3 ) * 4 ) + 5 ) + 6 )'))
