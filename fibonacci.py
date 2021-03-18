# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:22:05 2021

@author: home
"""

def fibbo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
         
            
number = int(input("enter number of terms:"))       
for i in range(1,number+1):
    print(fibbo(i))