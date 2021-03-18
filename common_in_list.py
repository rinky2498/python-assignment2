# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:09:03 2021

@author: home
"""
##write a program that returns a list that contains only the elements that are common between the lists 
list1 = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list3 = set(list1) & set(list2)  #  & calculates the intersection.
print(list3)

