# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 21:51:41 2014

@author: Max
"""

from PIL import Image
image = Image.open("C:/Users/Max/Desktop/rpsls.jpg")  
def pixel_selector(center,radius,position):
    x=center[0]
    y=center[1]
    x_position=position[0]
    y_position=position[1]
    if (x-x_position)**2+(y-y_position)**2<=radius**2:
        return True
    else:
        return False  
        
def picture_editor(image,center,radius,color):
    x_range_1=center[0]+radius
    x_range_2=center[0]-radius
    y_range_1=center[1]+radius
    y_range_2=center[1]-radius
    color_red=color[0]
    color_green=color[1]
    color_blue=color[2]
    for i in range(x_range_2,x_range_1):
        for j in range(y_range_2,y_range_2):
            position=[i,j]
            circle_verify=pixel_selector(center,radius,position)
            if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
                image.putpixel((i,j),(color_red,color_green,color_blue))
    #I think that it isn't saving in between pixels

radius=20
#Spock location
center=[85,220]
color=(255,0,0)
picture_editor(image,center,radius,color)

#for i in range(25,150):
#    for j in range(155,280):
#        position=[i,j]
#        circle_verify=pixel_selector(center,radius,position)
#        if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
#            image.putpixel((i,j),(0,255,0))
#Paper Location
center=[320,220]
#for i in range(250,380):
#    for j in range(155,280):
#        position=[i,j]
#        circle_verify=pixel_selector(center,radius,position)
#        if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
#            image.putpixel((i,j),(255,0,0))
#Rock location
center=[200,125]
#for i in range(130,270):
#    for j in range(55,195):
#        position=[i,j]
#        circle_verify=pixel_selector(center,radius,position)
#        if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
#            image.putpixel((i,j),(255,0,255))
#Lizard location
center=[125,350]
#for i in range(50,195):
#    for j in range(280,420):
#        position=[i,j]
#        circle_verify=pixel_selector(center,radius,position)
#        if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
#            image.putpixel((i,j),(0,255,255))
#Scissors location
center=[275,350]
#for i in range(205,345):
#    for j in range(280,420):
#        position=[i,j]
#        circle_verify=pixel_selector(center,radius,position)
#        if image.getpixel((i,j))>=(150,150,150) and circle_verify==True:
#            image.putpixel((i,j),(255,255,0))

image.save("C:/Users/Max/Desktop/rpsls_green.jpg")
image.show()