# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 12:28:55 2014

@author: Max
"""
integer_list=[]
for i in range(1,200001):
    integer_list.append(i)
 
length=len(integer_list)-1  

long_integer='1'
for j in range(1,length):
    long_integer=long_integer+str(integer_list[j])
    
print(len(long_integer))
    
print(long_integer[1:100])

answer=int(long_integer[9])*int(long_integer[99])*int(long_integer[999])*int(long_integer[9999])*int(long_integer[99999])*int(long_integer[999999])
print(answer)