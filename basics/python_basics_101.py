#!/usr/bin/env python3

# The above opening line is called shebang. Used to tell the shell which program to use to execute this file. This helps in executing the file directly at the command prompt.
# This is a comment in Python

# This file basics_101 has some basic code covering the very basic concepts of Python - Printing, Variables, datatypes

# 1 Print a constant (a number) or a string directly (not through a variable)

print("\n Printing constants/string directly")
print(3)
print(3.4)
print("My name is Laks")
print("Hello World!")

# 2 Variables, assignment and datatypes - Integer, Float, String, List (Mutable sequence), Tuple (Immutable sequence), Dictionary (Key value - value any tyoe)

print("\n This is about Integers")
int_variable = 2
print(type(int_variable))
print(int_variable)

print("\n This is about Floats")
float_variable = 3.1
print(type(float_variable))
print(float_variable)

print("\n This is about Strings")
string_variable = "I am a example string"
print(type(string_variable))
print(string_variable)

print("\n This is about Lists - mutable sequences")
sample_list_ints = [1,3,5,7,9]
sample_list_strings = ["abc", "def", "xyz"]
fruits_list = ["Mango", "Orange", "Banana"]
print(type(fruits_list))
print(fruits_list)

print("\n This is about Tuples - immutable sequences")
sample_tuple_ints = (1,3,5,7,9)
sample_list_strings = ("abc", "def", "xyz")
fruits_tuple = ("Mango", "Orange", "Banana")
print(type(fruits_tuple))
print(fruits_tuple)

print("\n This is about Dictionaries - key value pairs")
sample_dict = {"10.128.0.0":"hostname_network", "10.128.0.1":"hostname_router", "10.128.0.2":"hostname_first_compute_eng"}
print(type(sample_dict))
print(sample_dict)


#Python Docstring is the documentation string which is string literal, and it occurs in the class, module, function or method definition, and it is written as a first statement."""
