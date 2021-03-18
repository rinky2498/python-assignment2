# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:55:23 2021

@author: home
"""

def stringReverse(string):
    list1 = string.split()
    list1.reverse()
    return list1

original_string = input('Please enter a phrase: ')
reversed_string = stringReverse(original_string)
print(reversed_string)
