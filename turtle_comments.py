import turtle
def carre(animal,size):
    for i in range (4):
        animal.forward(size)
        animal.left(90)
#1
"""def petitscarres(animal,n,size):
    a=0
    for i in range (n):
        carre(animal,size)
        animal.penup()
        animal.forward(40)
        animal.pendown()"""

#2
"""def carresconc(animal,n,size):
    a=size
    for i in range(n):
        carre(animal,size)
        animal.penup()
        animal.left(-90)
        animal.forward(a/2)
        animal.left(90)
        animal.forward(-a/2)
        size=size+20
        animal.pendown()"""
#3
"""def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)"""
#4
"""def bigstar(t,n,sz):
    for i in range (n):
        for k in range (4):
            carre(t,sz)
            t.left(-90)
        t.left(-90/n)"""
#5
"""def spiral(t,n,angle,size,space):
    t.left(-180)
    for i in range (n):
        t.forward(size)
        t.left(-90-angle)
        size+=space"""
