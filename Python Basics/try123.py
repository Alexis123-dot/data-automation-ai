import turtle
import turtle
import math
t = turtle.Turtle()

def polygon(t, n, length):
    angle= 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

        
polygon(t, 7, 70)


def circle(t, r):
    n=60
    length=(2*math.pi*r)/n
    angle= 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


circle(t, 100)
