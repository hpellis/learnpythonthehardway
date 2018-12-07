# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:00:23 2018

@author: 612383249
"""

#this line creates a string variable
ten_things="Apples Oranges Crow Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

#this line creates a new variable called stuff which contains each item from ten_things separately
stuff=ten_things.split(' ')

#this line creates a new list called more_stuff which contains some separate list items
more_stuff=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while stuff is not equal to 10, this function will do the following
while len(stuff) !=10:
#creates a variable called next_one which is equal to the last item in the new list
    next_one=more_stuff.pop()
#this line prints out that the next_one item is getting added
    print("Adding: ", next_one)
#this line appends next_one to the stuff list
    stuff.append(next_one)
#this line prints out that the list stuff has a length of X many items now
    print(f"There are {len(stuff)} items now.")
 
#when there are 10 items on the list, the while loop stops
#this line prints out the list stuff, which has the items added on
print("There we go: ", stuff)

#
print("Let's do some things with stuff.")

#this prints the item at index 1 in the list stuff
print(stuff[1])
#this prints the item at the last index position in the list stuff
print(stuff[-1])
#this line also prints out the last item from the list
print(stuff.pop())
#this line prints out a slice from index 3-5 in list stuff [5 exclusive], and then joins those items together with a # between them 
print('#'.join(stuff[3:5]))







