# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 09:07:42 2014

@author: Max
"""

d_1=[3,-4,2]
d_2=[2,1,-1.5]
def magnitude(vector):
    from math import sqrt
    almost_magnitude=vector[0]**2+vector[1]**2+vector[2]**2
    magnitudinal=sqrt(almost_magnitude)
    return magnitudinal
b=magnitude(d_1)
print(b)
c=magnitude(d_2)
print(c)

def dot_product(vector_one,vector_two):
    multi=vector_one[0]*vector_two[0]+vector_one[1]*vector_two[1]+vector_one[2]*vector_two[2]
    return multi

b=dot_product(d_1,d_2)
print(b)