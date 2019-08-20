# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

############################################################
#Modelling planetery orbits                                #
#Fahad Chohan 07/12/2015                                   #
############################################################

#I am making a two planet system around a star by using Newton's equations of motion to calculate forces between the bodies

#importing 
from visual import sphere, vector, color, rate, mag

dt = 0.0001 # timestep
step = 1 # loop counter
maxstep = 1000000 # maximum number of steps

#  Define the star, planets and constants
M = 10000 # mass of star (in units where G = 1)
mass1 = 10 # mass of planet 1
pos1 = vector(0,5,0) # initial position vector of planet 1
Planet1 = sphere(pos=pos1,radius=0.025*mass1,color=color.blue,make_trail=True)
Planet1.trail_object.color=color.blue # make the trail blue
Star = sphere(pos=(0,0,0),radius=0.5,color=color.yellow)
vel1 = vector(-50, 0, 0) # initial velocity of planet 1
G = 1

#initial time 
t = 0

#mass, initial velocity and position of planet 2 (second body)
mass2 = 0.1 # mass of planet 2
pos2 = vector(0,5.1,0.1) # initial position vector of planet 2
Planet2 = sphere(pos=pos2,radius=1*mass2,color=color.white,make_trail=True)
Planet2.trail_object.color=color.white # make the trail white
vel2 = vector(35, 0, 0) # initial velocity of planet 2

#Making a loop
while step <= maxstep:
   
   
   #I have added another term to the velocity equation so that the velocity of the body is affected by BOTH other bodies
   
   #Velocity and position calculations of planet 1 based on force from other two bodies 
   vel1 = vel1 - dt*(G*M*pos1)/(mag(pos1)**3) - dt*(G*mass2*pos1)/(mag(pos1)**3)
   pos1 = pos1 + vel1*dt
   
   #Velocity and position calculations of planet 2 based on force from other two bodies 
   vel2 = vel2 - dt*(G*M*pos2)/(mag(pos2)**3) - dt*(G*mass1*(pos2 - pos1))/(mag(pos2 - pos1)**3)
   pos2 = pos2 + vel2*dt
      
   #time step
   t = t + dt 
   
   #displayin planet and moon
   Planet1.pos = pos1      
   Planet2.pos = pos2   
   
   #rate and increasing step number
   rate(2500)
   step = step + 1

print("end of program")