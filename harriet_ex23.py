# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:28:44 2018

@author: 612383249
"""

import sys
script, input_encoding, error=sys.argv

#this function reads one line from the language_file
def main(language_file, encoding, errors):
    line=language_file.readline()
 
#this if statement checks that the main function isn't at the end of the file
    if line:
#if it is not at the end of a file then it calls the print_line function and returns the value into the main function, which it calls again (this loops through until at the end of the text file)
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
 
#this function encodes each line from the language_file
def print_line(line, encoding, errors):
#this line gets rid of \n
    next_lang=line.strip()
#encode the language from the language_file into raw bytes
    raw_bytes=next_lang.encode(encoding, errors=errors)
#this line turns the raw bytes into a string by decoding them
    cooked_string=raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)
    
languages=open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)