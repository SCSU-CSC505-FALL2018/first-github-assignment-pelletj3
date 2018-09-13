#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:18:54 2018

@author: jacobpelletier
"""
def ignition():
    '''
    allows user input to provide flow control in program:
        if s is entered, the program continues
        if q is entered, the program ends
    input: none
    output: user input as flow control, returns either s or q
    '''
    ignition_flag = True
     
    while ignition_flag == True:
        # prompts the user to start program or quit program
        program_ignition = input('\nTo start a conversion enter s. To quit enter q. '
                                 '\n\nEnter selection here: ')
        if program_ignition == 'q':
            return('q')
            ignition_flag = False
        elif program_ignition == 's':
            return('s')
            ignition_flag = False
        else:
            print('\nEnter a valid input.')

# debug test
# print(ignition())
 