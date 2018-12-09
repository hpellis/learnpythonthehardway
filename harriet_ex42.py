#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:07:12 2018

@author: harriet
"""

#creates a class called Animal which is an object

class Animal(object):
    pass

#cCreates a class Dog which is a subclass of the class Animal, and has an init function with the params self and anem
class Dog(Animal):
    
    def __init__ (self, name):

#this line sets the self.name attribute of the class Dog to name      
        self.name=name
        
#this creates a class called Cat, which is a sub class of the class Animal and has an init function with the params self and name
class Cat(Animal):
    
    def __init__ (self, name):

#this sets the self.name attribute of the class Cat to name      
        self.name=name
  
#this creates a class called Person which is an object, and has an init function with the params self and name
class Person(object):    
    
    def __init__ (self, name):

#this sets the self.name attribute of the class Person to name      
        self.name=name
        

#this creates a class Employee which is a subclass of the Person class and has an init function with the params self, name and salary
class Employee(Person):
    
    def __init__ (self, name, salary):

# this uses super to call the init method from the superclass     
        super(Employee, self).__init__(name)

#this sets the self.salary attribute of the class Employee to salary        
        self.salary=salary

#this creates a class called Fish  
class Fish(object):
    pass

#this creates a class called Salmon which is a subclass of the Fish class 
class Salmon (Fish):
    pass

#this creates a class called Halibut which is a subclass of the Fish class   
class Halibut(Fish):
    pass



#instance variables below are "has-a" relationships


#creates a variable called rover which is an instance of the Dog class, and sets the param of name to "Rover"
rover=Dog("Rover")

#creates a variable called satan which is an instance of the Cat class, and sets the param of name to "Satan"
satan=Cat("Satan")

#creates a variable called mary which is an instance of the person class, and sets the param of name to "Mary"
mary=Person("Mary")

#from mary gets the pet attribute and sets it to Satan
mary.pet=satan

#creates a variable called frank which is an instance of the Employee class and sets the params of name and salary
frank=Employee("Frank", 1200000)

#from frank gets the pet attribute and sets it to rover
frank.pet=rover

#creates a variable called flipper which is an instance of the Fish class
flipper=Fish()

#creates a variable called crouse which is an instance of the Salmon class
crouse=Salmon()

#creates a variable called harry which is an instance of the Halibut class
harry = Halibut()
        
        
    