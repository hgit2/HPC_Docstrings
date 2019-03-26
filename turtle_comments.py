
import turtle

def carre(animal,size):
    """Args:
        animal (str): name of the animal, must be one word without spaces.
        size (int): size of the square, must be an integer.
       
       Return:
        draw a square of size "size", the drawing made by the chosen animal.
        """
    for i in range (4):
        animal.forward(size)
        animal.left(90)

def petitscarres(animal,n,size):
    """Args:
        animal (str): name of the animal, must be one word without spaces.
        n (int) : number of square to draw, must be an integer.
        size (int): size of the square, must be an integer.
       
       Return:
        draw n square of size "size", the drawing made by the chosen animal.
        """
    a=0
    for i in range (n):
        carre(animal,size)
        animal.penup()
        animal.forward(40)
        animal.pendown()

def carresconc(animal,n,size):
    """Args:
        animal (str): name of the animal, must be one word without spaces.
        n (int) : number of square to draw, must be an integer.
        size (int): size of the first square (the smallest) , must be an integer.
       
       Return:
        draw n concentric squares of initial size "size", the drawing made by the chosen animal.
        """
    a=size
    for i in range(n):
        carre(animal,size)
        animal.penup()
        animal.left(-90)
        animal.forward(a/2)
        animal.left(90)
        animal.forward(-a/2)
        size=size+20
        animal.pendown()

def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def bigstar(t,n,sz):
    for i in range (n):
        for k in range (4):
            carre(t,sz)
            t.left(-90)
        t.left(-90/n)

def spiral(t,n,angle,size,space):
    t.left(-180)
    for i in range (n):
        t.forward(size)
        t.left(-90-angle)
        size+=space
