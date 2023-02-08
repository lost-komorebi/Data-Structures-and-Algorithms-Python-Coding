#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
Base on my infix evaluator from infix_postfix_prefix_convertor.py
to implement a very simple calculator.
"""
from infix_postfix_prefix_convertor import infix_evaluator


class Calculator:
    def __init__(self):
        self.expression = []

    def calculate(self):
        result = infix_evaluator(' '.join(self.expression))
        return result

    def get_user_input(self):
        if not self.expression:
            user_input = input('Please enter:')
        else:
            saved_expression = ' '.join(self.expression)
            user_input = input(
                f'Your saved expression is {saved_expression}. ' +
                '\n' +
                f'Please enter:')
        if user_input.isdigit() or user_input in '+-*/':
            self.expression.append(user_input)
        return user_input

    def checker(self, string):
        return string.isdigit() or string in '+-*/q='

    def main(self):
        print(
            "This calculator only support operators('+-*/') and operands(numbers)! " +
            '\n' +
            "Enter 'q' to quit! Enter '=' to get result! " +
            '\n' +
            "Any other characters are unsupported!")
        user_input = self.get_user_input()
        while user_input not in ('q', '=') or not self.checker(user_input):
            user_input = self.get_user_input()
            if user_input == 'q':
                break
            if user_input == '=':
                print(f"Your result is: {self.calculate()}.")
                break


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.main()
