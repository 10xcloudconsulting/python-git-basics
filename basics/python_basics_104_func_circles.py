#!/usr/bin/env python3

#This file explores the concept of functions a little further using circles as the basis. It uses concepts of Lists, Dictionaries and String formatting.

#To use the Python inbuilt module "math" use import math. Get pi value from there.
import math
#Import the area_circle Function defined in the python_basics_104_functions.py to use in in this file
from python_basics_104_functions import area_circle

# 1 Use the area_circle function
print("The area of the circle with radius 3 is: {:.2f}".format(area_circle(3)))

# Taking input from the user and calling the functions in this file
input_radius_str = input("Enter the radius: ")
#Convert input that is read as string into Integer
input_radius = int(input_radius_str)
print("The area of the circle with radius {} is: {:.2f}".format(input_radius,area_circle(input_radius)))
#Printing using String.format method differently
print("Circle with radius {rad} has an area of {area_cir:.2f}".format(rad=input_radius,area_cir=area_circle(input_radius)))

# 2 Calculating the area of a circle for a list of cicles
list_of_radius = [1,2,3,4,5]
i = 1
for radius in list_of_radius:
    print("Area of circle {} is: {:.2f}".format(i, area_circle(radius)))
    i = i + 1

# 3 Storing the radii and the corresponding areas of a set of circles in a Dictionary and printing it
circle_dict = {1:0, 2:0, 3:0, 4:0, 5:0}
print("Size of the circle dictionary is: {}".format(len(circle_dict)))
for key in circle_dict:
    print("Key is: {}, Value is: {}".format(key, circle_dict[key]))
