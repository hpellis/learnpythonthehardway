#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:36:58 2018

@author: harriet
"""

#this creates a class called Parent
class Parent(object):

#class Parent has a function override which prints out a statement    
    def override(self):
        print("PARENT override()")

#class Parent has a function implicit which prints out a statement       
    def implicit(self):
        print("PARENT implicit()")

#class Parent has a function altered which prints out a statement        
    def altered(self):
        print("PARENT altered()")

#this creates a class called Child which is a subclass of the Parent class        
class Child(Parent):

#Child class has a function called override which prints out a statement
    def override(self):
        print("CHILD override()")

#Child class has a function called altered which prints out three statements     
    def altered(self):

#the first statement is this
        print("CHILD, BEFORE PARENT altered()")

#the second statement calls the altered function of the super class, which is the Parent class
        super(Child, self).altered()
        
#this third statement is this
        print("CHILD, AFTER PARENT altered()")

#this creates a variable called dad which is an instance of the Parent class        
dad=Parent()

#this creates a variabled called son which is an instance of the Child class
son=Child()

#from dad this calls the implicit function
dad.implicit()

#from son this calls the implicit function, which doesn't exist in the Child class but is inherited from the Parent class
son.implicit()

#from dad this calls the override function
dad.override()

#from son this calls the seperate override function that is specified in the Child class
son.override()

#from dad this calls the altered function
dad.altered()

#from son this calls the separate altered function which is specified in the Child class
son.altered()

