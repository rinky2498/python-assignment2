# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:26:28 2021

@author: home
"""

##write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list

def find(orderedlist,element_to_find):
   for element in orderedlist:
      if(element==element_to_find):
         return True
   
         return False

thislist = [1,8,10,15,30,45,50]
print(find(thislist,20))
print(find(thislist,45))
print(find(thislist,8))
print(find(thislist,10))