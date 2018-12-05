# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:08:02 2018

@author: 612383249
"""

people =30
cars=40
trucks=15

if cars > people:
    print("We should take the cars.")
    
elif cars < people:
    print("We shuld not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant decide.")
    
if people < trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    