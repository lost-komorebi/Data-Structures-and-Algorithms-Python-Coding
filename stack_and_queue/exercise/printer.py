#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
using python to simulate a printer
1. create a printing queue
2. for every second
    1. check if have new printing task, if yes, using current_second as its timestamp, and add task into queue
    2. if printer is not busy, and there are printing tasks in queue
        1. get first task from queue, and let printer to print
        2. use current_second to minus current_task's timestamp , to calculating time need to be wait
        3. add waiting_time to a list, so we can calculate average waiting_time later
        4. calculate time to finish current task according to the pages of current task
    3. for every second, printer finishes one second printing pages and current task's waiting_time also minus one
    4. if printer finishes current task or time_remaining minus to 0, then printer is not busy
3. calculate average waiting time
"""

import random


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Task:
    def __init__(self, time):
        self.timestamp = time  # to store when this task was generated
        self.pages = random.randrange(1, 21)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        """ calculate how many seconds the printer will take to finish current task """
        return current_time - self.timestamp


class Printer:
    def __init__(self, ppm: int):
        self.current_task = None
        self.time_remaining = 0  # the amount of seconds for printer to finish task
        self.printing_speed = ppm  # pages per minute

    def tick(self):
        """ counting down """
        if self.current_task:
            self.time_remaining -= 1
            if self.time_remaining < 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task:
            return True
        return False

    def start_next(self, new_task: Task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() / self.printing_speed * 60


def simulation(num_seconds, ppm):
    printer = Printer(ppm)  # init printer
    print_queue = Queue()  # init q to store printing task queue
    waiting_times = []  # store all waiting_time

    for current_second in range(num_seconds):
        if generate_new_task():
            task = Task(current_second)  # init a new task
            print_queue.enqueue(task)  # put new task into queue

        if not printer.is_busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()  # get a print task from queue
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait_time = sum(waiting_times) / len(waiting_times)
    print(
        'Average Wait {:.2f} seconds {} tasks remaining.'.format(
            average_wait_time,
            print_queue.size()))


def generate_new_task():
    """ generate a print task randomly """
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 10)
