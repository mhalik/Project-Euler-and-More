# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 09:18:04 2014

@author: Max

"""
import time
# First, we will ask for the bill
bill=round(float((input("What is your bill? "))),2)
# Then, we ask about how much tip you are willing to pay
tip=float(input("What tip would you like to give in percentage of 100? "))
bill_and_tax=bill*1.0625
bill_total=((100+tip)/100)*bill_and_tax
# After calculating tip and tax, the program will print your cost
print("Your bill is %.2f in american dollars." % bill_total)

# This will put the time into "asc" format, then print it.
b=time.asctime( time.localtime(time.time()) )
print("The current time is:", b)

# This will always return "true".
MakeMeTrue = 3==3 or 4!=5
print("MakeMeTrue is %s" % MakeMeTrue)