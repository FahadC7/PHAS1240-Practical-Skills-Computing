# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:46:52 2015

@author: zcapfch
"""

############################################################
#Calculating Madelung constant for a crystal of NaCl crystal
#Fahad Chohan 23/11/2015
############################################################

#In this session I will be calculating the Madelung constant for an NaCl crystal.
#I will also create a visual display of the structure


# Importing numpy and functions for creating a sphere of different colours
import numpy as np
from visual import sphere, color, curve, rate

##MAKING 7 BY 7 BY 7 CRYSTAL STRUCTURE

#Setting limit for deciding the amount of ions in structure
num = 3

#Setting sphere size for Na and Cl ions, Na ions are smaller
sizeNa = 0.3
sizeCl = 0.4

# loop over each spatial dimension
for i in range(-num, num+1):
    for j in range(-num, num+1):
        for k in range (-num, num+1):
            
            #This function allows us to only select even coordinates to make into Na ions            
            if (i+j+k)%2.0 == 0:

                #Setting position, size and colour for Na ions
                sphere(pos=[i,j,k],radius=sizeNa,color=color.white)
            
            #This selects all the other coordinates (odd), to make into Cl ions
            else:

                #Setting position, size and colour for Na ions
                sphere(pos=[i,j,k],radius=sizeCl,color=color.green)

##MAKING 25 BY 25 BY 25 CRYSTAL STRUCTURE

#Setting initial conditions for use in loop
Vpt = 0
Vnt = 0
Vp = 0
Vn = 0
L = 12

# loop over each spatial dimension
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range (-L, L+1):
            
            #This function allows us to only select even coordinates to make into Na ions            
            if (i+j+k)%2.0 == 0:

                #Setting position, size and colour for Na ions
                sphere(pos=[i,j,k],radius=sizeNa,color=color.white)
            
            #This selects all the other coordinates (odd), to make into Cl ions
            else:

                #Setting position, size and colour for Na ions
                sphere(pos=[i,j,k],radius=sizeCl,color=color.green)
                
            #Making a loop to calculate the sum of all positive (Sodium ions) values for calculating the Madelung constant for NaCl crystal
            if (i+j+k)%2.0 == 0 and (i**2 + j**2 + k**2) != 0:
                Vp =  1.0/np.sqrt(i**2 + j**2 + k**2)
                Vpt = Vpt + Vp
            
            #Making a loop to calculate the sum of all negative (Chlorine ions) values for calculating the Madelung constant for NaCl crystal
            if (i+j+k)%2.0 != 0 and (i**2 + j**2 + k**2) != 0:
                Vn =  1.0/np.sqrt(i**2 + j**2 + k**2)
                Vnt = Vnt + Vn

#This sums the values for the above 2 loops so that the negative dont cancel out the posotive values, this calculates the approx Madelung constant value for a NaCl crystal of dimension 25x25x25
M = Vpt - Vnt

#These are the values for the Madelung constant approximation
print "Calculated value for NaCl of M =", M
print "Accepted value for NaCl of M ~", -1.748
print "Difference in calculated and accepted value of M =", M+1.748

#As you can see our calculated Madelung constant is very close to the accepted value of the Madelung constant for NaCl