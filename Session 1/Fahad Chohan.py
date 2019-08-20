# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 15:01:20 2015

@author: zcapfch
"""
###########################################################################
#Calculating speed, direction and time taken of an object using SUVAT model
#Fahad Chohan 05/10/15
###########################################################################

from math import sqrt

#input
#acceleration of free fall on Earth (m/s^2)
g = -9.81
#initial Velocity (m/s)
v0 = 10
#initial height (m)
z0 = 15
#verticle displacement (m)
z = 0.0

#Calculates velocity squared using SUVAT equation
v2 = v0**2 + 2*g*(z-z0)

#speed is equal to the square root of the velocity
speed = sqrt(v2)

#Determining if the velocity is negative or posotive in referrence to initial conditions of variables
if v0 > 0:
    print "v0 is positive"
else:    
    print "v0 is less than or equal to zero"

#Using SUVAT to calulate time taken
time_taken = -(speed + v0)/g

#Output to screen
print "speed is equal to: ", speed, "m/s"
print "time taken is equal to:", time_taken, "s"
