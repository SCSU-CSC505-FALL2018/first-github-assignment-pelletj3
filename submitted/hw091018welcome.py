#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:48:54 2018

@author: jacobpelletier
"""

def welcomestatement():
    '''
    input: none
    output: 
            1) Welcome message explains purpose of program and instructions
            2) returns either y or q which either start or quit program, respectively
    '''   
    # initial welcome statement explaining pupose and instructions
    return('\nWelcome to the decimal-binary conversion program! When prompted, you '
          'will enter a decimal integer, then the program will convert that decimal integer '
          'into its binary equivalent. Pretty cool stuff! '
          '\nRules:\n\t-decimal to binary only\n\t-positive numbers only\n\t-integers only')

#debug test
#print(welcomestatement())

