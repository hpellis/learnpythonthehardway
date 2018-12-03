# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:33:06 2018

@author: 612383249
"""

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print ("Type the filename again:")
file_again=input(">")

txt_again = open(file_again)

print(txt_again.read())