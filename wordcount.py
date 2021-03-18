# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 08:38:50 2021

@author: home
"""
##given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen
count = 0

file = open('fruit.txt', 'r')


for line in file:  
    #Splits each line into words  
    words = line.split(" ");  
    #Counts each word  
    count = count + len(words);  
   
print("Number of words present in given file: " + str(count)); 


file.close()

