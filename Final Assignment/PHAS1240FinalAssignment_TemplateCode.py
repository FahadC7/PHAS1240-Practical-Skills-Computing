##################################################
#    PHAS1240 2015 final assignment
#    Frozen Angry Birds Star Wars
#    Template code
##################################################


import numpy as np
from visual import sphere, vector, color, rate, mag, display

#!@!@### TEMPLATE HEADER STARTS ###@!@!#

scene = display(width = 640, height = 480, center = (5,0,0),autoscale=False, range = 6)

### Set up objects ### 

# Set implicit gravitational constant G = 1
# All values are in Galactic Natural Units except where stated otherwise

## The Death Snowball ###
M = 2000 # mass of Death Snowball 
DSrad = 1.0 # radius of Death Snowball
DSpos = vector(7.0,0.0,0.0) # position vector of Death Snowball
DeathSnowball = sphere(pos=DSpos,radius=DSrad,color=color.white,make_trail=True)
vel_DS = vector(0.0,0.0,0.0) # initial velocity of Death Snowball


### The Death Star ###
M2 = 2000 # mass of Death Star
DS2rad = 0.5 # radius of Death Star
DS2pos = vector(10.0,-2.0,0.0) # position vector of Death Star
vel_DS2 = vector(0,15.0,0.0) # initial velocity of Death Star 
DeathStar = sphere(pos=DS2pos,radius=DS2rad,color=color.gray(0.5),make_trail=True)

## Olaf, the Sith Snowman ###
# You will need to complete this section yourself following the specification in the script
OlafAngle = np.radians(45) # angle of Olaf's position relative to DS centre
OlafRad = 0.1 # Olaf's radius
Olafx= # Olaf's x-coordinate COMPLETE THIS LINE
Olafy= # Olaf's y-coordinate COMPLETE THIS LINE
Olaf = sphere(pos=(Olafx,Olafy,0),radius= OlafRad,color=color.white,opacity=0.5) 

### Angry Jedi bird ###
mbird = 1 # mass of angry bird, may be *much* bigger than 1 later
initpos = vector(0,0,0) # initial position vector of bird
Bird= sphere(pos=initpos,radius=0.1,color=color.red,make_trail=True)
Bird.trail_object.color=color.white # make the trail white

## Set initial parameters of bird ##
v0 = # add a suitable number here
theta = np.radians() # add a suitable angle here

## Set velocity, timestep etc ##
vel_bird = vector(v0*np.cos(theta), v0*np.sin(theta), 0) # initial velocity of Bird
dt = 0.001 # timestep in seconds
step = 1 # loop counter
maxstep = 300 # maximum number of calculation steps to include

#!@!@### TEMPLATE HEADER ENDS ###@!@!#

