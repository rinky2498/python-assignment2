# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:05:32 2021

@author: home
"""

t_no = int(input("enter the numner:  "))
for i in range(1,11):
    print(t_no*i)
    
    f = open("table.txt","a")
    f.write(str(t_no*i))
    f.close()
    