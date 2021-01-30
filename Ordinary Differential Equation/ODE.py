from turtle import *
import numpy as np
import math
hideturtle()

def bluelines():
    screensize(2000,2000)
    hideturtle()
    speed(0)
    color('pink')
    for i in range(31):
        pu()
        goto(-15+i,-15)
        pd()
        goto(-15+i,15)
        pu()
    for j in range(31):
        pu()
        goto(-15,-15+j)
        pd()
        goto(15,-15+j)
        pu()
def setup():
    screensize()
    p=1
    hideturtle()
    speed(0)
    setworldcoordinates(-7,-7,7,7)
    setpos(0,0)
    clear()
    bluelines()
    setpos(0,0)
    setheading(0)
    pd()
    color('black')
    for i in range(15):
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        setpos(0,0)
        fd(p)
        write(-p)
        lt(90)
        p=p+1
setup()

# Differential equation of a pendulum (NON IDEAL CASE)
g=-9.8
L=1
mu=0.4
THETA_0=math.pi/2
THETA_DOT_0=0.01
def get_theta_double_dot(theta,theta_dot):
    return -mu*theta_dot-(g/L)*np.sin(theta)

def theta(t):
    theta=THETA_0
    theta_dot=THETA_DOT_0
    delta_t=0.01
    for time in np.arange(0,t,delta_t):
        theta_double_dot=get_theta_double_dot(theta,theta_dot)
        theta+=theta_dot*delta_t
        theta_dot+=theta_double_dot*delta_t
    return theta,theta_dot

x=0.1
dx=0.01
while x<=math.pi*12:
    hideturtle()
    pensize(1)
    screensize(2000,2000)
    color('black')
    while x<0:
        def draw_1(matA):
            pu()
            speed(0)
            goto(theta(x)[0],theta(x)[1])
            pd()
            for point in matA:
                speed(0)
                goto(point[0],point[1])
        def get_theta_double_dot(theta,theta_dot):
            return -mu*theta_dot-(g/L)*np.sin(theta)

        def theta(t):
            theta=THETA_0
            theta_dot=THETA_DOT_0
            delta_t=0.01
            for time in np.arange(0,t,delta_t):
                theta_double_dot=get_theta_double_dot(theta,theta_dot)
                theta+=theta_dot*delta_t
                theta_dot+=theta_double_dot*delta_t
            return theta,theta_dot
        
        ayush=[[theta(x+dx)[0],theta(x+dx)[1]]]
        draw_1(ayush)
        x=x+dx
    while x>0 and x<=math.pi*12:
        def draw_1(matA):
            pu()
            speed(0)
            goto(theta(x)[0],theta(x)[1])
            pd()
            for point in matA:
                speed(0)
                goto(point[0],point[1])
        def get_theta_double_dot(theta,theta_dot):
            return -mu*theta_dot-(g/L)*np.sin(theta)

        def theta(t):
            theta=THETA_0
            theta_dot=THETA_DOT_0
            delta_t=0.01
            for time in np.arange(0,t,delta_t):
                theta_double_dot=get_theta_double_dot(theta,theta_dot)
                theta+=theta_dot*delta_t
                theta_dot+=theta_double_dot*delta_t
            return theta,theta_dot        
        ayush=[[theta(x+dx)[0],theta(x+dx)[1]]]
        draw_1(ayush)
        x=x+dx
