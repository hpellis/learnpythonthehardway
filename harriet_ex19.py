# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:05:41 2018

@author: 612383249
"""
#this function prints out the number of cheese and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
 
#this line uses the function name and passes two arguments to it
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#this line calls the function and uses as the arguments two global variables
print("Or, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this line calls the function name and passes two arguments to it
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#this line calls the function, and uses as arguments the two global variables set above and performs addition on them
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers +1000)


def animals_at_the_zoo(a,b):
    print(f"Today at the zoo I saw a {a} and a {b}.")
    
animals_at_the_zoo("zebra", "hippo")

animal1="giraffe"
animal2="monkey"

animals_at_the_zoo(animal1, animal2)

