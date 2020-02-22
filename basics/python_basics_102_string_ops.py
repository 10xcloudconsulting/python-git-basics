#!/usr/bin/env python3

# The above opening line is called shebang. Used to tell the shell which program to use to execute this file. This helps in executing the file directly at the command prompt.
# This is a comment in Python
"""This is also a comment in Python"""
"""This can be used for
a
multi line
comment"""

# This file basics_102 has some basic code covering Operations on the String

#Common String operations"""

""" 1 len(string) Returns the length of the string"""

str_len = "This is an example string"
#print("Length of this example string is: {}" len(str))
print(len(str_len))

""" 2 for character in string Iterates over each character in the string"""

str_for_loop = "Cherry"
for x in str_for_loop:
    print("The current char is: " + x)


""" 3 if substring in string Checks whether the substring is part of the string"""


""" 4 string[i] Accesses the character at index i of the string, starting at zero"""

""" 5 string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default."""

#String Class Methods (Common ones only)

""" 1 string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters"""

""" 2 string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace"""

""" 3 string.count(substring) Returns the number of times substring is present in the string"""

""" 4 string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False."""

""" 5 string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False."""

""" 6 string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter"""

""" 7 string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new."""

""" 8 delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter"""


"""Formatted string literal
A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format method strings. The important difference with the format method is that it takes the value of the variables from the current context, instead of taking the values from parameters.
"""

item = "Purple Cup"
amount = 5
price = amount * 3.25

print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')
