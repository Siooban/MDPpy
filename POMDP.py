# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:06:01 2022

@author: Sioban
"""
import numpy as np

#creation du plateau 
grille=np.zeros([5, 9])

#0 pour un mur 1 pour un passage

grille[1,1]=1
grille[2,1]=1
grille[3,1]=1

grille[1,2]=1

grille[1,3]=1
grille[2,3]=1
grille[3,3]=1

grille[1,4]=1

grille[1,5]=1
grille[2,5]=1
grille[3,5]=1

grille[1,6]=1

grille[1,7]=1
grille[2,7]=1
grille[3,7]=1

print(grille)

reward=np.zeros([5, 9])
reward[3,3]=10
reward[3,5]=-100
print(reward)

action=["up","bottom", "left", "right"]


#deterministic transition function
def transitionFunctionD(states, action, currentState):
    if action=="up":
        stateUp=(currentState[0]-1, currentState[1])
        if states[stateUp[0], stateUp[1]]==0:
            return currentState
        else:
            return stateUp
    if action=="bottom":
        stateDown=(currentState[0]+1,currentState[1])
        if states[stateDown[0],stateDown[1]]==0:
            return currentState
        else:
            return stateDown
    if action=="left":
        stateLeft=(currentState[0], currentState[1]-1)
        if states[stateLeft[0], stateLeft[1]]==0:
            return currentState
        else: 
            return stateLeft
    if action=="right":
        stateRight=(currentState[0], currentState[1]+1)
        if states[stateRight[0], stateRight[1]]==0:
            return currentState
        else: 
            return stateRight
        
        
print(transitionFunctionD(grille,"left", (1,3)))


#stochastic transition function
#observationFunction
"""this function return the wall number surrounding a position"""
def ObservationFunction(states, currentState):
    wallDistribution=[]
    stateUp=(currentState[0]-1, currentState[1])
    if states[stateUp[0], stateUp[1]]==0:
        wallDistribution.append("up")
    stateDown=(currentState[0]+1,currentState[1])
    if states[stateDown[0],stateDown[1]]==0:
        wallDistribution.append("bottom")
    stateLeft=(currentState[0], currentState[1]-1)
    if states[stateLeft[0], stateLeft[1]]==0:
        wallDistribution.append("left")
    stateRight=(currentState[0], currentState[1]+1)
    if states[stateRight[0], stateRight[1]]==0:
        wallDistribution.append('right')
    return wallDistribution
    
print(ObservationFunction(grille, (2,3)))
print(ObservationFunction(grille, (1,1)))
print(ObservationFunction(grille, (3,3)))
def Game(states, reward, action):
    return "victory"