# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:19:59 2019

@author: Pranavi.Gandham
"""

import numpy

#Create list that contains the 4 songs in the running playlist
songs = [1, 2, 3, 4]

#Counter values to be used to see when 3, 2 and 1 unique songs are picked respectively
threeUnique = 0
twoUnique = 0
oneUnique = 0

#Simulate professor listening to 3 songs 10,000 times
for i in range(10000):
    lst = []
    for l in range(3):
        choice = numpy.random.choice(songs)
        lst.append(choice)
    #Conditional to see how many unique songs were picked
    if len(set(lst)) == len(lst):
        threeUnique += 1
    elif len(set(lst)) == 2:
        twoUnique += 1
    else:
        oneUnique +=1

#Compute the probability that professor listens to 3, 2, 1 unqiue songs respectively
probThreeUniqueSongs = threeUnique/10000
probTwoUniqueSongs = twoUnique/10000
probOneUniqueSongs = oneUnique/10000
print("After 10,000 simulations, the probability that after 3 songs are played that your professor listens to three unique songs is %s ." %probThreeUniqueSongs)

#Calculate average number of unique songs that professor listens to when 3 songs are played
expectedValue = (1/4*1) + (1/3*2) + (1/2*3) 
print("The average number of unique songs that your professor listens to when 3 songs are played is %s" %expectedValue)

    
    
    
    
    

    
    
    
    



