from turtle import *
from random import randrange
from freegames import square,vector

f = vector(0,0)
s = [vector(10,0)]
a = vector(0,-10)

def change(x,y):  # Change Snake's Direction
    a.x=x
    a.y=y

def inside(h):    # Returns True if Head Inside Boundaries
    return ((-200<h.x<190) and (-200<h.y<190))

def move():       # Move the Snake Forward One Step  
    h=s[-1].copy()
    h.move(a)

    if not inside(h) or h in s:
        square(h.x,h.y,9,'red')
        update()
        return
    s.append(h)

    if h == f:
        print('snake',len(s))
        f.x=randrange(-15,15)*10
        f.y=randrange(-15,15)*10
    else:
        s.pop(0)
    clear()

    for body in s:
        square(body.x,body.y,9,'green')

    square(f.x,f.y,9,'red')
    update()
    ontimer(move,100)

    hideturtle()
    tracer(False)
    listen()

# Key Controls For the User to play the Game

onkey(lambda :change(10,0),'Right')         
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()