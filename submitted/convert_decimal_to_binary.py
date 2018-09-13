#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:21:05 2018

@author: jacobpelletier
"""

'''
int to hexadecimal 



'''


import hw091018welcome as welfx
import hw091018ignition as igfx
import hw091018input as infx
import hw091018converter as confx

# master switch; True when program running, False when stopped
program = True

# initial welcome statement explaining program pupose and instructions
print(welfx.welcomestatement())

# program logic
while program == True:
    print('_______________________________________________')
    if igfx.ignition() == 's':
        int_to_eval = (infx.user_input())
        print('\n' + str(int_to_eval) + ' in binary form is ' + 
              confx.dec_to_bin_converter(int_to_eval))     
    else:
        print('\nThank you! Goodbye.')
        program = False
        
