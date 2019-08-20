# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:44:57 2015

@author: zcapfch
"""
################################################
#Calculating 1/4 of pi
#Fahad Chohan 12/10/2015
################################################

#Key
#value is the final desired term, pi/4
#n is the number of terms used in the calculation
#tolerance is the accuracy to which the term is desired
#newterm is next value added from the series

from numpy import pi

value = 0 #Setting initial conditions
n = 0 #Setting initial conditions
tolerance = float(raw_input('Tolerance:')) # User to input tolerance
newterm = tolerance + 1 # This is making sure initial conditions for loop are satisfied

while abs(newterm) >= tolerance: #Conditions fo loop
    newterm = (-1)**n * (2.0*n + 1)**(-1) #Calculating the next term in the sequence
    value = value + newterm #Summing the sequence
    n = n + 1 # Starting the next iteration
    print "adding", newterm, "to", value #Showing what is going on in each loop

print "Number of terms used:", n
print "Approximation for pi/4:", value
print "Numpy value for pi/4:", pi/4
#Printing values

#This is not good for approximating a value for pi because it would take approximately 2.61*10**15 seconds (8.27*10**7 years) for approximating pi to a tolerance of 10e-20 which is obviously too long.