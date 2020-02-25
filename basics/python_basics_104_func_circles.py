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

# 4 Interactive session with a User to calculate and return area of circles

print("Welcome to the Interactive Session to get the Area of a Circle")

cont = "y"
while(cont.lower() == "y"):
    radius_interact = input("Please enter the radius of the circle to get the area: ")
    area_interact = area_circle(int(radius_interact))
    print("The area is : {:.2f}".format(area_interact))
    cont = input("Do you want to do one more calculation [y to continue]: ")

print("Thank you. See you again!")

# 5 Working with environment variables
import os
print("HOME: " + os.environ.get("HOME", ""))

# 6 Working with command line arguments
import sys
print("Command Line arguments are")
print(sys.argv) #Returns a list

# 7 Working with files
file = open("input_radius_file.txt")
print("The radius is: " + file.readline())
print("The radius is: " + file.readline())
print("The radii are: " + file.read())
file.close()

with open("input_radius_file.txt") as file:
    print("The radii in the file are: " + file.read())

# Iterate through the file (file object which is a sequence)
with open("input_radius_file.txt") as file:
    print(type(file))
    for radius_line in file:
        print(radius_line)

# Keep the lines in the file in a list and can be iterated separately as needed. Use readlines for only small files. All file content is loaded to memory!
with open("input_radius_file.txt") as file:
    lines = file.readlines()
    print(type(lines))
    lines.sort()
    print(lines)
    for line in lines:
        print(line)

# Use strip to remove the newline character
with open("input_radius_file.txt") as file:
    for radius_line in file:
        print(radius_line.strip())

# Writing into a file. File open modes and arguments (w, a, r+, r and other modes).  w creates a file if not existing; overides if one exists.
with open("output_circle_area.txt", "w") as out_file:
    out_file.write("Radius: 4" + "Area: " + str(area_circle(4)))


# 8 Working with Dictionaries. Use os module
import os
print("The current working directory is : " + os.getcwd())
print("List of directories and files in CWD: ")
print(os.listdir(os.getcwd()))
dir = os.getcwd()
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# 9 Working with CSV files. Use Radius and Area as Headers.
import csv

circle_list = [[1,"area1"], [2,"area2"]]
with open("./data/circle_rad_area.txt", "w") as file:
    writer = csv.writer(file)
    writer.writerows(circle_list)

with open("./data/circle_rad_area.txt", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        radius, area = row
        print("Radius: {} Area: {}".format(radius, area))

circles_list = [{"radius":10,"area":"area1"}, {"radius":20,"area":"area2"}, {"radius":30,"area":"area3"}]
keys = ["radius", "area"]
with open("./data/circle_rad_area.txt", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(circles_list)

# 10 Working with env variable INPUT_FILE getting radii and calculating areas and publishing all back into file into file given in env variable OUTPUT_FILE
