# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:06:01 2022

@author: Sioban
"""
import numpy as np
import random

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

#print(grille)

reward=np.zeros([5, 9])
reward[3,3]=10
reward[3,5]=-100
#print(reward)

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

"""return the array of observation from the initial position """
def Initialisation(states):
    result=np.zeros((5,9))
    t=[]
    shape=np.shape(states)
    print(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if states[i,j]==1:
                t.append((i, j))
    value=random.randint(0, len(t)-1)
    observation=ObservationFunction(states, t[value])
    if "up" in observation:
        if "bottom" in observation:
            result[1,2]=1/3
            result[1,4]=1/3
            result[1,6]=1/3
            return t[value], result
        elif "right" in observation:
            result[1,7]=1
        elif "left" in observation:
            result[1,1]=1
            return t[value], result
        else: 
            result[1,3]=1/2
            result[1,5]=1/2
            return t[value], result
    
    if "bottom" in observation:
        if "right" in observation:
            if "left" in observation:
                result[3,1]=1/4
                result[3,3]=1/4
                result[3,5]=1/4
                result[3,7]=1/4
                return t[value], result
    if "right" in observation:
        if "left" in observation:
            result[2,1]=1/4
            result[2,3]=1/4
            result[2,5]=1/4
            result[2,7]=1/4
            return t[value], result
            
    return t[value], result
    
init=Initialisation(grille)
print(init)   

def compare(ob1,ob2):
    result =  all(elem in ob1  for elem in ob2)
           
    return result



""" update the probability array after an action"""
def Update(states, probabilities, newObservation,action):
 
    shape=np.shape(states)
    result=np.zeros(shape)
    nbValue=0
    indice=[]
    for i in range(shape[0]):
        for j in range(shape[1]):
            if probabilities[i, j]!=0:
                newState=transitionFunctionD(states,action, (i,j))
                testObservation=ObservationFunction(states, newState)
                print(testObservation,newObservation)
                
                test=compare(testObservation, newObservation)
                if test:
                    indice.append(newState)
                    nbValue+=1
                print( indice)
    for k in range(len(indice)):
        result[indice[k][0], indice[k][1]]=1/nbValue
    return result

currentPos=init[0]
newPos=transitionFunctionD(grille,"bottom", currentPos)
print(newPos)
ob=ObservationFunction(grille, newPos)     
newGrille=Update(grille,init[1],ob, "bottom")
print("new grille")
print(newGrille)
    
    
    
def Game(states, reward, action):
    return "victory"