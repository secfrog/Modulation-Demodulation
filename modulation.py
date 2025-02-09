from turtle import *
from math import *

bgcolor("black")

t1 = Turtle()
t1.width(2)
t1.color("white")
t1.hideturtle()
t1.speed(0)

t12 = Turtle()
t12.width(2)
t12.color("yellow")
t12.hideturtle()
t12.speed(0)

t2 = Turtle()
t2.width(2)
t2.color("green")
t2.hideturtle()
t2.speed(0)

t3 = Turtle()
t3.width(2)
t3.color("orange")
t3.hideturtle()
t3.speed(0)


def s(t, Sm, fs):
    return Sm*cos(2*pi*fs*t)
    
def s12(t, Sm, U0, fs):
    return Sm*cos(2*pi*fs*t) + U0

def p(t, Pm, fp):
    return Pm*cos(2*pi*fp*t)

def us(t, k, U0, s, Sm, fs, p, Pm, fp):
    return k*(s(t, Sm, fs) + U0) * p(t, Pm, fp)






def init(turtle,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()





texty=30

def onde1_courbe(s,Sm, fs, ydecalage=0):
    init(t1,0,-80)
    t1.write("Tension modulante", align="center", font=('Arial', 12, 'normal'))

    c=True
    for t in range(-200,200):
        y = s(t,Sm,fs) +ydecalage
        if c:init(t1, t,y); c=0
        t1.goto(t,y)

def onde12_courbe(s,Sm,U0,fs, ydecalage=0):
    init(t12, 0,-80-texty)
    t12.write("Tension modulante redressée", align="center", font=('Arial', 12, 'normal'))
    c=True
    for t in range(-200,200):
        y = s12(t,Sm,U0,fs) +ydecalage
        if c:init(t12, t,y); c=0
        t12.goto(t,y)


def onde2_courbe(p,Sm, fp, ydecalage=0):
    init(t2, 0,-80-texty*2)
    t2.write("Tension porteuse", align="center", font=('Arial', 12, 'normal'))
    c=True
    for t in range(-200,200):
        y = p(t,Sm,fp) +ydecalage
        if c:init(t2, t,y); c=0
        t2.goto(t,y)

def onde3_courbe(us, k, U0, s, Sm, fs, p, Pm, fp, ydecalage=0):
    init(t3, 0,-80-texty*3)
    t3.write("Tension modulée", align="center", font=('Arial', 12, 'normal'))
    c=True
    for t in range(-200, 200):
        y = us(t,k,U0,s,Sm,fs,p,Pm,fp) + ydecalage
        if c:init(t3, t,y); c=0
        t3.goto(t,y)

# Repère orthonormé 10/div
def repere():
    turx = Turtle()
    tury = Turtle()
    turgr = Turtle()
    
    turx.color('white')
    tury.color('white')
    turgr.color('white')
    turgr.hideturtle()

    init(tury, -200,-100)
    tury.goto(-200,200)
    tury.setheading(90)
    
    init(turx,-200,0)
    turx.goto(250,0)

    for x in range(-200, 240, 10):
        init(turgr, x, -5)
        turgr.goto(x,5)

    turgr.penup()
    turgr.forward(40)
    turgr.pendown()
    turgr.write("t(s)", align="center", font=('Arial', 12, 'normal'))
    turgr.penup()
    turgr.forward(40)
    turgr.right(90)
    turgr.forward(40)
    turgr.pendown()
    turgr.write("10s/div", align="center", font=('Arial', 12, 'normal'))

    for y in range(-100, 190, 10):
        init(turgr, -205, y)
        turgr.goto(-195,y)
    
    turgr.penup()
    turgr.setheading(180)
    turgr.forward(40)
    turgr.pendown()
    turgr.write("U(V)", align="center", font=('Arial', 12, 'normal'))
    turgr.penup()
    turgr.forward(20)
    turgr.setheading(270)
    turgr.forward(30)
    turgr.pendown()
    turgr.write("10V/div", align="center", font=('Arial', 12, 'normal'))
    

# exemple bonne modulation,;: Sm, fs, U0, k, Pm, fp, = 25, 1/100, 35, .02, 50, 1/4
# Tp = 1/fp doit être paire pour que p(t) oscille entre Pm et -Pm
Sm, fs, U0, k, Pm, fp, = 25, 1/100, 35, .02, 50, 1/4

def start_script():
    repere()
    onde1_courbe(s,Sm,fs)
    onde12_courbe(s12,Sm,U0,fs)
    onde2_courbe(p,Pm, fp)
    onde3_courbe(us, k, U0,  s,Sm,fs,  p,Pm,fp)

screen = Screen()

screen.listen()
screen.onkey(start_script, "Return")
screen.mainloop()

exitonclick()