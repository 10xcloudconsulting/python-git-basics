#!/usr/bin/env python3

#This file explores operating with files, functions, loops, command line args, lists, dictionaries, csv files, etc

#Get the values of the radii whose areas need to be calculated from a file. The name of the file is provided as a command line argument
import sys
from python_basics_104_functions import area_circle
import csv

if (len(sys.argv) < 3):
    print("\nUsage: python_basics_104_files_circles.py <input_file> <output_file>\n")
    print("Please provide the input and output file names\n")
    sys.exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

output_file_header = ["Radius of the Circle", "Area of the Circle"]
output_list = []
output_line_dict = {}

with open(input_file) as i_file:
    line_num = 0
    for radius in i_file.readlines():
        print("The radius is : {}".format(radius.strip()))
        radius_int = int(radius)
        area = area_circle(radius_int)
        print(type(area))
        print("The area is : {:.2f}\n".format(area))
        print("Line number is : " + str(line_num))
        print("output_list length is : " + str(len(output_list)))

        output_list.append({"Radius of the Circle":radius_int,"Area of the Circle":area})
        print(output_list[line_num])
        line_num = line_num + 1

with open(output_file, "w") as o_file:
    writer = csv.DictWriter(o_file, fieldnames=output_file_header)
    writer.writeheader()
    writer.writerows(output_list)

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
