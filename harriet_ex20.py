# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:28:14 2018

@author: 612383249
"""
#imports the argv function from sys
from sys import argv

#unpacks the argv variable and assigns arguments to variables script and input_file
script, input_file=argv

#creates a function called print_all which reads and prints out the contents of a file
def print_all(f):
    print(f.read())

#this creates a function called rewind which goes to the first byte in a file
def rewind(f):
    f.seek(0)
    
#this creates a function which takes two arguments and prints the line number and contents of the line
def print_a_line(line_count, f):
    print(line_count, f.readline())

#this creates a new variable called current_file which is the open version of input_file
current_file=open(input_file)

#this prints out a message to the user
print("First let's print the whole file:\n.")

#this calls the print_all function on the current_file variable, printing out what is in the file
print_all(current_file)

#this prints out a message to the user
print("Now let's rewind, kind of like a tape.")

#this calls the rewind function on the current_file variable, which makes the pointer go to line 0
rewind(current_file)

#this prints out a message to the user
print("Let's print three lines:")

#this sets the variable current_line as 1
current_line=1

#this calls the print_a_line function with the current_line and current_file arguments, printing out what is on the first line
print_a_line(current_line, current_file)

#this prints out what is on the next line
current_line=current_line + 1
print_a_line(current_line, current_file)

#this prints out what is on the next line
current_line=current_line +1
print_a_line(current_line, current_file)