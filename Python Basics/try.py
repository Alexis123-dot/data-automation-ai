import turtle

t= turtle.Turtle()


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

        
print (square)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
square(t, 130)
