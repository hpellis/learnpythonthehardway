# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:27:35 2018

@author: 612383249
"""

#this creates a variable called states that is a dictionary containing state names mapped to state abbreviations
states={
        "Oregon":"OR",
        "Florida":"FL",
        "California":"CA",
        "New York":"NY",
        "Michigan":"MI",
        }

#this creates a variable called cities which is a dictionary containing state abbreviations mapped to city names
cities={
        "CA": "San Francisco",
        "MI": "Detroit",
        "FL": "Jacksonville",
        }

#these lines add new entries to the cities dictionary, including the abbreviation and the city it maps to

cities["NY"]="New York"
cities["OR"]="Portland"

#this prints out a dashed line
print('-' * 10)

#this prints out the string plus the item in the city dict mapped to NY
print("NY State has: ", cities["NY"])
#this prints out the string plus the item in the city dict mapped to OR
print("OR State has: ", cities["OR"])

print('-' *10)

#these print out strings plus the item in the states dict that maps to the state names
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

print('-' *10)

#these print out strings then uses both the cities and states dicts to get the cities mapped to the state names. Have to use both lists because the state names aren't directly mapped to the cities.
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

print('-' *10)

#this creates a for loop, which for every state and abbrev in the states dict, the string is printed
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")
        
#print every city in state
print('-' * 10)

#this creates a for loop, which for every abbrev and city in the cities dict, the string is printed
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")
    
print('-' * 10)

#this creates a for loop, which for every state and abbrev in the states dict, the string is printed
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
#this line references the cities dict to get the abbrev
    print(f"and has city {cities[abbrev]}.")

print('-' * 10)

#this is a method of trying to get an abbrev for a state that is not in the dict
#it creates a variable called state, and calls the "get" function on the states dictionary, passing "Texas" as the argument to it
state=states.get("Texas")

#this prints out a message
#if not checks for truth - i.e. if not true
if not state:
    print("Sorry, no Texas.")
    
#this creates a variable called city, and calls function get on the cities dictionary. It passes it two arguments, the abbrev that the city is mapped to and the phrase "does not exist". The phrase is passed to the space in the string because the first argument doesn't return anything.
city=cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}.")


        



    








