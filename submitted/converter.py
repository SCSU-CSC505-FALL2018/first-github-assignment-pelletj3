#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:21:05 2018

@author: jacobpelletier
"""

'''
To do:
int to hexadecimal
hexadecimal to int
'''
import hw091018welcome as welfx
import hw091018ignition as igfx
import hw091018input as infx
import hw091018Dec_to_Bin_converter as confx
import hw091018Bin_to_Dec_converter as binfx

# master switch; True when program running, False when stopped
program = True

# initial welcome statement explaining program pupose and instructions
print(welfx.welcomestatement())

# program logic
while program == True:
    print('_______________________________________________')
    conversion_choice = igfx.ignition()
    if conversion_choice == 'binary':
        int_to_eval = (infx.user_input())
        print('\n' + str(int_to_eval) + ' in binary form is ' +
              confx.dec_to_bin_converter(int_to_eval))
    elif conversion_choice == 'decimal':
        int_to_eval = (infx.user_input())
        print('\n' + str(int_to_eval) + ' in binary form is ' +
              binfx.bin_to_dec_converter(int_to_eval))
    else:
        print('\nThank you! Goodbye.')
        program = False
