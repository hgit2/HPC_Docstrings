#!/usr/bin/python3
# -*- coding: utf-8 -*-

# General Imports
import turtle 

def carre(animal,size):
    """ draws a square of size "size", the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle object. 
        size (int): size of the square, must be a positive integer.
    """
    for i in range (4):
        animal.forward(size)
        animal.left(90)

def petitscarres(animal,n,size):
    """draws n square of size "size", the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle object.
        n (int) : number of square to draw, must be a positive integer.
        size (int): size of the square, must be a positive integer.
    """
    a=0 # A quoi sert a?
    for i in range (n):
        carre(animal,size)
        animal.penup()
        animal.forward(40)
        animal.pendown()

def carresconc(animal,n,size):
    """draws n concentric squares of initial size "size", the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle object.
        n (int) : number of square to draw, must be a positive integer.
        size (int): size of the first square (the smallest) , must be a positive integer.
    """
    a=size # A quoi sert a?
    for i in range(n):
        carre(animal,size)
        animal.penup()
        animal.left(-90)
        animal.forward(a/2)
        animal.left(90)
        animal.forward(-a/2)
        size=size+20
        animal.pendown()

def draw_poly(animal,n,sz):
    """draws a "n"-gon with sides of size size "size", the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle object.
        n (int) : number of sides of the polygon, must be a positive integer.
        size (int): size of the sides of the n-gon, must be a positive integer.
    """
    for i in range(n):
        animal.forward(sz)
        animal.left(360/n)

def bigstar(animal,n,size):
    """draws a star made up from "n" squares, which sides are of size "size", the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle objecanimal
        n (int) : number of squares used to draw the star, must be a positive integer.
        size (int): size of the sides of the n-gon, must be a positive integer.
    """
    
    for i in range (n):
        for k in range (4):
            carre(animal,size)
            animal.left(-90)
        animal.left(-90/n)

def spiral(animal,n,angle,size,space):
    """draws a spiral made up from "n" lines of increasing size, the drawing made by the chosen animal.
    
    Args:
        animal (turtle): name of the animal, must be a turtle object.
        n (int): number of lines used to draw the spiral, must be a positive integer.
        angle (int): the angle between two consecutive lines, must be an integer. 
        size (int): size of the first line, must be a positive integer.
        space (int): every time a line is drawn, the size of the next size is increased by "space", must be a positive integer.
        
    Return:
        the animal's position.
        
    Examples:
        
        >>> import turtle
        >>> window=turtle.Screen()
        >>> tess=turtle.Turtle()
        >>> spiral(tess,10,13, 20,9)
        (60.18,19.15)
        
    """
    
    animal.left(-180)
    for i in range (n):
        animal.forward(size)
        animal.left(-90-angle)
        size+=space
    return animal.pos()


# code test
window=turtle.Screen()
tess=turtle.Turtle() # : modele d'initialisation d'une turtle
print(spiral(tess,10,13, 20,9))
turtle.mainloop()
