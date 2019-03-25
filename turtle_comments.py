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
#6
"""def draw_equitriangle(t,sz):
      draw_poly(t,3,sz)"""


"""window=turtle.Screen()
window.bgcolor("alice blue")
window.title("Hello, Tess!")
tess=turtle.Turtle()
tess.color("orchid")
draw_equitriangle(tess,100)
turtle.mainloop()"""


#7
"""def sum_to(n):
    sum=0
    for i in range (n+1):
        sum+=i
    return(sum)
print(sum_to(10))"""

#8
"""from math import pi
def area_of_circle(r):
    area=pi*r**2
    return(area)
print(area_of_circle(10))"""

#9
"""def star(t):
    for i in range (5):
        t.forward(100)
        t.left(-144)"""

#10
"""def many_stars(t):
    for k in range(5):
        star(t)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()"""

#11
"""def many_stars(t):
    for k in range(5):
        star(t)
        t.forward(350)
        t.right(144)"""



"""window=turtle.Screen()
window.bgcolor("alice blue")
window.title("Hello, Tess!")
tess=turtle.Turtle()
tess.color("orchid")
many_stars(tess)
turtle.mainloop()"""

#1
"""L=["N","E","S","O"]
def turn_clockwise (point):
    p=0
    k=0
    for i in range(len(L)):
        if L[i]==point:
            k=i
        elif point not in L:
            return(None)
    p=L[(k+1)%4]
    return(p)

print(turn_clockwise ('T'))"""

#2
"""def day_name(n):
    L=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if n<len(L):
        return(L[n])
    else:
        return(None)

print(day_name(8))"""

#3
"""def inv_day_name(day):
    L=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if day not in (L):
        return(None)
    else:
        for i in range (len(L)):
             if L[i]==day:
                return(i)

print(inv_day_name("Wednesday"))
"""
#4
"""
L=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def day_add(day,n):
    i=inv_day_name(day)
    if i!=None:
        i=L[(i+n)%7]
    return(i)

print(day_add("Monday",-6))"""

#5
"""j'ai utilise des congruences qui fonctionnent avec les nombres negatifs"""

#6
"""def days_in_month(month):
    days=0
    L=["January","February",...]
    n=0
    for i in range (len(L)):
        if month==L[i]:
            n=L[i]
        else:
            days=None
    if n==0 or n==2 or n==4 or n==6 or n==7 or n==9 or n==11:
        days=31
    if n==1:
        days=28
    else:
        days=30
    return (days)"""
#7
"""def to_sec (h,m,s):
    sum=3600*h+60*m+s
    return(sum)

print(to_sec(2,30,10))"""

#8
"""def ext_to_sec(h,m,s):
    sum=3600*h+60*m+s
    sum=sum//1
    return(sum)

print(ext_to_sec(2.5,0,10.71))"""

#9
"""def hours_in(n):
    hour=n//3600
    return(hour)

def minutes_in(n):
    minute=(n-hours_in(n)*3600)//60
    return(minute)

def seconds_in(n):
    second=n-hours_in(n)*3600-minutes_in(n)*60
    return(second)"""

#10
"3%4==0 est faux car % correspond au modulo(c'est egale a 3 ou -1)"
"3/4==0 est faus car / corrspond a la division (// division entiere)"
"3+4*2==14 est faux car ca fait 11 (si on veut 14 il faut mettre des parenthese autour de 3+4)"
"4-2+2==0 est faux car ca fait 4"

#14
"""def is_even(n):
    if n%2==0:
        return(True)
    else:
        return(False)
print(is_even(11))
"""
#15
"""def is_odd(n):
    return(not is_even(n))
print(is_odd(4))"""

#p107
"""s="http://coucou yoyo"
def_pos=s.find("http://")
if def_pos ==0:
    op_index=s.find(" ")
    fname=s[0:op_index]
    print(fname)"""


"""s="coucou<tralala>boum"
def_pos=s.find("<")
op_index=s.find(">")
fname=s[def_pos+1:op_index]
print(fname)"""

"""#p108
import random
joe=random.Random()
def sum1():
    xs=[]
    for i in range(10000000):
        num=joe.randrange(1000)
        xs.append(num)
    tot=sum(xs)
    return(tot)

def sum2():
    tot=0
    for i in range(10000000):
        num=joe.randrange(1000)
        tot+=num
    return(tot)

print(sum1())
print(sum2())"""
    
"""sum1:6,1   sum2:4,1  on prefere donc ici sum2"""
""" la somme 1 ne peut continuer au dela de ..."""


       

