#!/usr/bin/env python3

#This file explores the concept of functions with some examples

#To use the Python inbuilt module "math" use import math
import math

# 1 Function to return the area of triangle

def area_triangle(base, height):
    return base * height/2

print("The area of the triangle with base 2 and height 5 is : {}".format(area_triangle(2,5)))

# 2 Function to return area of a circle

def area_circle(radius):
    return math.pi*radius**2

print("The area of the circle with radius 3 is: {:.2f}".format(area_circle(3)))
