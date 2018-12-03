# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:43:43 2018

@author: 612383249
"""
#this lines imports argv
from sys import argv

#this line imports the 'exists' command. This returns True if a file exists, based on its name in a string as an argument.
from os.path import exists

#this line unpacks argv so that rather than holding all the arguments, it gets assigned to the variables you are working with
script, from_file, to_file=argv

#this prints to the user what this script does
print(f"Copying from {from_file} to {to_file}.")

#this creates a variable called in_file, which is equal to the open from_file
in_file=open(from_file)

#this creates a variable called indata which is equal to reading in_file. This is how you know how many bytes the from_file is
indata=in_file.read()

#this prints out to the user how many bytes long the from_file is 
print(f"The input file is {len(indata)} bytes long.")


#this line provides a True/False response to whether the file being copied to exists
print(f"Does the output file exist? {exists(to_file)}")

#Input is required to move on, otherwise the user cancels the programme
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#this line creates a new variable called out_file which opens the to_file
#the 'w' means you are opening the file in 'write' mode (as opposed to read or append)
out_file=open(to_file, 'w')

#this line writes the contents of indata to the to_file
out_file.write(indata)

#this line prints confirmation to the user
print("Alright, all done.")

#these lines close the two file objects created 
out_file.close()
in_file.close()