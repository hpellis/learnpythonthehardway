# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:16:51 2018

@author: 612383249
"""
#this line creates the variable i and makes it 0
i=0
#this line creates the variable numbers and sets it to an empty list
numbers=[]

#this is a while statement which dictates functions to happen while the value of i is lower than 6
while i< 6:
#this line prints the lowest value for i
    print(f"At the top i is {i}.")
#this line appends i to the numbers list
    numbers.append(i)
 
#this line adds 1 to i each time it is run
    i=i + 1
#this line prints out the list of numbers, which includes the one added previously
    print("Numbers now: ", numbers)
#this line prints out the value of i now that it has had one added     
    print(f"At the bottom i is {i}.")

#when the while loop is no longer true, this line prints out the text    
print("The numbers: ")

#this is a for loop. it sets the variable num as part of the list numbers
for num in numbers:
#this lines prints out every variable num in the list, printing out everything in the list
    print(num)