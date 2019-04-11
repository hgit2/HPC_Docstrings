#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################################################################################################
####################################################    turtle_comments.py  TUTORIAL #############################################
##################################################################################################################################

# General Imports
import turtle 

# turtle_comments.py Import
import turtle_comments

##################################################################################################################################

##### First you need to create your animal, a turtle object that will draw your figures #####

### Start by initializing a window
window=turtle.Screen()

### Then instantiate your animal (a lion here)
lion=turtle.Turtle() 

##### Then you can call the drawing function of your choice #####

### imagine that you want to draw a square with sides of size 3
print(turtle_comments.carre(lion,25))
### does the drawing
turtle.mainloop()

### then you want to draw a star made up from 5 squares, which sides are of size 50
print(turtle_comments.bigstar(lion,5,50))
turtle.mainloop()

### finaly you want to draw 8 squares with sides of size 100 and an hexagone with sides of size 40
print(turtle_comments.petitscarres(lion,8,100))
print(turtle_comments.draw_poly(lion,6,40))
turtle.mainloop()

#print(spiral(tess,10,13, 20,9))
#turtle.mainloop()
