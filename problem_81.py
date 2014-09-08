# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 22:05:41 2014

@author: Max
"""
import numpy


filename='C:/Users/Max/Desktop/p081_matrix.txt'
fin=open(filename,'r')
matrix=[]
i=0
while i<=81:
    my_string=fin.readline()
    length=len(my_string)+1
    my_new_string=my_string.split(',')
    matrix=concatenate((matrix,my_new_string))
    i=i+1
print(matrix)
   
        


    