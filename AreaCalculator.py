"""
Program designed to calculate area of circle or triangle. Prompts user for shape, calculates area, and prints area to user.

Author: Andrew Jones
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Good morning, Dave. The calculator is starting up..."
print "The current time is: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option.upper()
if option == 'C':
    radius = float(raw_input("Please input the radius: "))
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
    base = float(raw_input("Please input the base of the Triangle: "))
    height = float(raw_input("Please input the height of the Triangle: "))
    area = (0.5)*base*height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f \n%s" % (area, hint))
else:
    print "Error! That input is garbage! The program will now exit..."