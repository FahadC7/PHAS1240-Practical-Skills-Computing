# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
############################################################
#Moving Vpython objects around screen using SUVAT equations#
#Fahad Chohan 30/11/2015                                   #
############################################################

# Importing numpy and functions for annimating a sphere
from visual import sphere, curve, color, display, rate
import numpy as np

# set up the scene
scene = display(x = 50, y = 50, width = 640, height = 480, center = (20,0,0))
ground = curve(pos=[(-5,0,0),(50,0,0)],color = color.green)

# initial ball coordinates (metres)
x0 = 0.0
y0 = 0.0
y = y0
g = 9.8 # gravitational acceleration, m/s2
dt = 0.01 # time interval for loop, in seconds
x = 0.0

# input initial angle and velocity
dtheta = float(raw_input("Input the initial angle in degrees: "))
theta = np.radians(dtheta)
theta1 = theta
v0 = float(raw_input("Input the initial velocity in metres/second: "))
e = float(raw_input("Input the value for coefficient of restitution: "))
v0min = float(raw_input("Input the value for the minimum value of velocity for the ball to be ablt to launch: "))

# start the animation
ball = sphere(pos = (x0,y0,0),radius = 1,make_trail=True)
t = 0.0 # initial time
#Loop only valid for when ball position is above or at ground
while v0 >= v0min:
    while y >= y0:
    
        #SUVAT equations for position of ball in x and y direction
        y = v0 * np.sin(theta) * t + 0.5 * -g * t**2
        x = x0 + v0 * np.cos(theta) * t
    
        #Adding small values to t so that ball position is calculated at small intervals
        t = t + dt
    
        #Displaying ball position and rate of annimation
        ball.pos = (x,y,0)
        rate(100)
    
    #This statement is only true for the first bounce and so outputs certain values for only first bounce    
    if theta1 == theta:
        #Calculating range using given equation
        r = (v0**2 * np.sin(2.0*theta))/(g)
        print "Time for first bounce =", t
        print "Range for first bounce =", r, "m"
        print "x = ", x, "m"
        print "Difference in x and range =", x-r, "m"
    
    #Reset y to 0 so that while loop can happen
    y = y0 
    
    #Values for the angle and launch velocity of each new bounce
    alpha = 0.5*np.pi - theta
    beta = np.arctan((np.tan(alpha))/e)
    v0 = v0*e*((np.cos(alpha))/(np.cos(beta)))
    theta = 0.5*np.pi - beta
    
    #Reset time and start next bounce from new value of x
    t = 0.0
    x0 = x

    
#Printing values for time of flight, range and actaul position on
print "END"

##########COMMENTS##################

#By changing dt we get smaller intervals for recalculating the ball position and therefore we get more accurate values for x as the range.
#For a smaller dt there would be more loop itterations too

#The code gives nearly very realistic results but the error caused by dt not being limited to 0 (error in x position) but as the number of bounces increase the error in the range increases.