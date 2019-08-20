##################################################
#    PHAS1240 2015 final assignment
#    Frozen Angry Birds Star Wars
#    Template code
##################################################

##################################################
#   Student number: 15019455
#   Last updated: 13/02/2016
##################################################

#CODE DESCRIPTION
#This code makes an angry birds knock-off and uses Newton's law of gravity to describe
#motion of objects.


#STORY INTRODUCTION
#Following an unfortunate lava-related incident, Olaf the Snowman has gone over to
#the Dark Side. Olaf is currently on the surface of his newly-built Death Snowball.
#An elite unit of Jedi Angry Birds has been despatched to defeat him. These Angry
#Birds explode on impact, and will destroy Olaf if their speed at the point of impact is
#sufficient. The evil Sith lord Darth Vader is most displeased with this development,
#and has teleported his Death Star into the region to support Olaf.
#The story continues . . .

import numpy as np
from visual import sphere, vector, color, rate, mag, display, label

#!@!@### TEMPLATE HEADER STARTS ###@!@!#

scene = display(width = 640, height = 480, center = (5,0,0),autoscale=False, range = 6)

### Set up objects ### 

# Set implicit gravitational constant G = 1
G = 1.0
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
Olafx= np.dot(DSpos,(1.0,0.0,0.0)) + (OlafRad + DSrad)*np.cos(OlafAngle) # Olaf's x-coordinate. Trigonometry used to position Olaf while accounting for radius of both.
Olafy= np.dot(DSpos,(0.0,1.0,0.0)) + (OlafRad + DSrad)*np.sin(OlafAngle) # Olaf's y-coordinate. Trigonometry used to position Olaf while accounting for radius of both.
Olaf = sphere(pos=(Olafx,Olafy,0),radius= OlafRad,color=color.white,opacity=0.5) 

### Angry Jedi bird ###
mbird = 1 # mass of angry bird, may be *much* bigger than 1 later
initpos = vector(0,0,0) # initial position vector of bird
Bird = sphere(pos=initpos,radius=0.1,color=color.red,make_trail=True)
Bird.trail_object.color=color.white # make the trail white

## Set initial parameters of bird ##
v0 = 110.7 # add a suitable number here
theta = np.radians(45) # add a suitable angle here

## Set velocity, timestep etc ##
vel_bird = vector(v0*np.cos(theta), v0*np.sin(theta), 0) # initial velocity of Bird
criticalspeed = 10 # Minimum speed of impact between Olaf and Bird for Olaf to be destroyed
dt = 0.001 # timestep in seconds
step = 1 # loop counter
maxstep = 500 # maximum number of calculation steps to include

#!@!@### TEMPLATE HEADER ENDS ###@!@!#




while step <= maxstep: # While loop
    rate(80) #Setting rate of animation to a suitable level
    
    #Calculating position and velocity of bird due to gravitational forces from Death Star and Death Snowball
    vel_bird = vel_bird - G*M*((Bird.pos-DeathSnowball.pos)/(mag(Bird.pos-DeathSnowball.pos)**3))*dt - G*M2*((Bird.pos-DeathStar.pos)/(mag(Bird.pos-DeathStar.pos)**3))*dt
    Bird.pos = Bird.pos + vel_bird*dt
    
    #Calculating position and velocity of Death Snowball due to gravitational forces bird
    vel_DS = vel_DS - G*mbird*((DeathSnowball.pos-Bird.pos)/(mag(DeathSnowball.pos-Bird.pos)**3))*dt
    DeathSnowball.pos = DeathSnowball.pos + vel_DS*dt
    
    #Calculating position and velocity of Death Star due to gravitational forces bird
    vel_DS2 = vel_DS2 - G*mbird*((DeathStar.pos-Bird.pos)/(mag(DeathStar.pos-Bird.pos)**3))*dt
    DeathStar.pos = DeathStar.pos + vel_DS2*dt 
    
    #Keeping Olaf in position on Death Snowball
    Olaf.pos = DeathSnowball.pos + vector((OlafRad + DSrad)*np.cos(OlafAngle),(OlafRad + DSrad)*np.sin(OlafAngle),0.0)
    
    step = step + 1 #Increasing step
    
    #Condition for Bird and Olaf to collide
    if mag(Bird.pos - Olaf.pos) <= Olaf.radius + Bird.radius:
        Bird.radius = 0.0 #Makes bird disappear
        
        #Condition for Bird to destroy Olaf
        if mag(vel_bird) >= criticalspeed:
            Olaf.radius = 0.0 #Makes Olaf disappear

            #Setting steps for explosion of Olaf and Bird
            n=1
            nmax=10
            
            #Creating loop for explosion animation
            while n <= nmax:
                rate(8)
                
                #Makes spheres of increasing radius and decreasing opacity to represent explosion animation
                explosion = sphere(pos=Olaf.pos,radius=0.05*n,color=color.red,opacity=0.6/n)
                n = n+1
            
            #Printing statement of occurance.            
            print "Sithlord Olaf has been slain by the brave Jedi Bird!!!"
            print "With an impact speed of", mag(vel_bird - vel_DS), "GDU/s."
            label(pos=(5.0,-3.0,0.0), text='Sithlord Olaf has been slain by the brave Jedi Bird!!!', height = 16)            
            label(pos=(5.0,-4.0,0.0), text='With an impact speed of ' + str(float('%.3g' %mag(vel_bird - vel_DS))) + ' GDU/s.', height = 16)
            
            break #Breaks loop and stops game
        
        #Condition for bird colliding with olaf but with a critical speed which is too low
        #Therefore Olaf does not explode but the Bird dies
        else:
            #Prints statement of what has occurred
            print"The Jedi Bird's speed was too little to defeat Olaf... "
            label(pos=(5.0,-3.0,0.0), text='The Jedi Birds speed of ' + str(float('%.3g' %mag(vel_bird - vel_DS))) + ' GDU/s was too little to defeat Olaf... ', height = 16)

            break #breaks loop and stops game
        
    #Condition for Bird colliding with Snowball
    if mag(Bird.pos - DeathSnowball.pos) <= DeathSnowball.radius + Bird.radius:
        Bird.radius = 0.0 #Disappearing Bird
        n=1
        nmax=10
        
        #Animation for bird exploding when hitting Snowball
        while n <= nmax:
            rate(8)
            
            #Makes spheres of increasing radius and decreasing opacity to represent explosion animation
            explosion = sphere(pos=Bird.pos,radius=0.05*n,color=color.white,opacity=0.6/n)
            n = n+1
        
        #Prints statement of what has occurred
        print "The Jedi Bird to crashed into the Death Snowball at", mag(vel_bird - vel_DS), "GDU/s."
        label(pos=(5.0,-3.0,0.0), text='The Jedi Bird to crashed into the Death Snowball at ' + str(float('%.3g' %mag(vel_bird - vel_DS))) + ' GDU/s.', height = 16)
        
        break #breaks loop and stops game
    
    #Condition for Bird hitting Death star
    if mag(Bird.pos - DeathStar.pos) <= DeathStar.radius + Bird.radius:
        Bird.radius = 0.0 #Makes bird disapper
        n=1
        nmax=10
        
        #loop for explosion animation
        while n <= nmax:
            rate(8)
            
            #Makes spheres of increasing radius and decreasing opacity to represent explosion animation
            explosion = sphere(pos=DeathStar.pos,radius=0.5*n,color=color.white,opacity=0.6/n)
            n = n+1
            
        #Prints statement of what has occurred
        print "Olaf escaped but at least the Jedi Bird destroyed the Death Star."
        label(pos=(5.0,-3.0,0.0), text='Olaf escaped but at least the Jedi Bird destroyed the Death Star \nat speed ' + str(float('%.3g' %mag(vel_bird - vel_DS2))) + ' GDU/s!', height = 16)
        
        break #breaks loop and stops game
    
    #If Bird doesnt collide with anything
    if step == maxstep:
        print "The Jedi bird has completely missed everything and now flies through space for eternity."
        label(pos=(5.0,-3.0,0.0), text='The Jedi bird has completely missed everything \nand now flies through space for eternity.', height = 16)
        