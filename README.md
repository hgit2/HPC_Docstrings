DESCRIPTION:
===========
turtle_comments provides the user with several functions that draw different types of figures:

* a square with "carre(animal,size)" 
* several squares with "petitscarres(animal,n,size)"
* concentric squares with "carresconc(animal,n,size)"
* a n-gon with "draw_poly(animal,n,sz)"
* a star with "bigstar(animal,n,size)"
* a spiral with "spiral(animal,n,angle,size,space)"

turtle_comments.py is written in Python3 and each of these functions require the turtle library.

IMPORT
=======
You can import turtle_comments with the following command :

import turtlecomments.turtle_comments


INSTALLATION:
============
type the command : 
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps turtle-comment-package-test-ha

FAQ:
===
Q - Can I draw a circle? 
A - Yes, you just need to call the draw_poly function with n set to a high value.

Q - Can I draw a rectangle?
A - Unfortunately, no.

CONTRIBUTE:
==========
turtle_comments.py is in the root directory of this repository :
[GitHub](https://github.com/hgit2/HPC_Docstrings).
You can find the doc in HPC_Docstring/docs/build/html/index.html

TODO:
====
Implement functions to draw additional kinds of figure such as rectangles (which are not squares).

LICENSE:
=======
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

