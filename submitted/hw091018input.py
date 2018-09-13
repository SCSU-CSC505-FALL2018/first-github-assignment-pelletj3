#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:52:33 2018

@author: jacobpelletier
"""

def user_input():
    '''
    input: takes in user input and tests to make sure it can be a valid int
    output: a string of a valid int
    '''
    input_flag = True
    while input_flag == True:
        user_decimal = input('Enter a decimal number to convert to binary: ')
        try:
            int(user_decimal)
            input_flag = False
            return int(user_decimal)
        except:
            print('Enter a valid integer.')
            
# Debug test
#print(user_input())