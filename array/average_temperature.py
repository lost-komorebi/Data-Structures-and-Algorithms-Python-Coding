#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

days = input("How many day's temperature?")
try:
    days = int(days)
except Exception as e:
    print(e)
else:
    temperature_list = []
    for i in range(days):
        temperature = input(f"Day {i}'s high temperature:")
        try:
            temperature = int(temperature)
        except Exception as e:
            print(e)
        else:
            temperature_list.append(temperature)

    average_temperature = sum(temperature_list) / days
    s = 0
    for i in temperature_list:
        if i > average_temperature:
            s += 1
    print(f'Average = {average_temperature}')
    print(f"Day's temperature above average")



