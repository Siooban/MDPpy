# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:53:38 2022

@author: Sioban
"""
import numpy as np
import random
""" """
class POMDP(object):
    def __init__(self,states, actions, rewards, TransitionF, ObservationF):
        self.states=states
        self.actions=actions
        self.rewards=rewards
        self.TransitionF=TransitionF
        self.ObservationF=ObservationF
        
    def getStates(self):
        return self.states
    def getActions(self):
        return self.actions
    def getRewards(self,transition):
        return self.rewards(transition)
    def getObservationF(self, currentState):
        return self.ObservationF(self.states, currentState)
    def getTransitionF(self,action, currentState):
        return self.TransitionF(self.states,action,currentState)
    
    
def makeObservationFunctionS():
        
    """ this function return the wall number surrounding a position
    with uncertainty """
    def ObservationFunctionS(states, currentState):
        proba=[]
        wallDistributions=[]
        wallDistribution=[]
        stateUp=(currentState[0]-1, currentState[1])
        if states[stateUp[0], stateUp[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateDown=(currentState[0]+1,currentState[1])
        if states[stateDown[0],stateDown[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateLeft=(currentState[0], currentState[1]-1)
        if states[stateLeft[0], stateLeft[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        stateRight=(currentState[0], currentState[1]+1)
        if states[stateRight[0], stateRight[1]]==0:
            wallDistribution.append(True)
        else:
            wallDistribution.append(False)
        result=wallDistribution.copy()
        wallDistributions.append(result)
        proba.append(0.8)  
        """ uncertainty"""
        value=random.randint(0,3)
        if wallDistribution[value]==False:
            wallDistribution[value]=True
        else:
            wallDistribution[value]=False
        wallDistributions.append(wallDistribution)
        proba.append(0.2)
    
        return wallDistributions, proba
    return ObservationFunctionS
    
def makeTransitionFunctionS():
    def transitionFunctionS(states, action, currentState):
        dictionnaire={}
        stateUp=(currentState[0]-1, currentState[1])
        stateDown=(currentState[0]+1,currentState[1])
        stateLeft=(currentState[0], currentState[1]-1)
        stateRight=(currentState[0], currentState[1]+1)
        if action=="up":
            value=0
            if states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.8
            else:
                value+=0.8
            if states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.1
            else:
                value+=0.1
            if states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
            
        if action=="bottom":
            value=0
            if states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.8
            else:
                value+=0.8
            if states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.1
            else:
                value+=0.1
            if states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        
        if action=="left":
            value=0
            if states[stateLeft[0], stateLeft[1]]==1:
                dictionnaire[(stateLeft)]=0.8
            else:
                value+=0.8
            if states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.1
            else:
                value+=0.1
            if states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
            
        if action=="right":
            value=0
            if states[stateRight[0], stateRight[1]]==1:
                dictionnaire[(stateRight)]=0.8
            else:
                value+=0.8
            if states[stateUp[0], stateUp[1]]==1:
                dictionnaire[(stateUp)]=0.1
            else:
                value+=0.1
            if states[stateDown[0], stateDown[1]]==1:
                dictionnaire[(stateDown)]=0.1
            else:
                value+=0.1
            if value!=0:
                dictionnaire[(currentState)]=value
        
        return dictionnaire
    return transitionFunctionS

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

rewardExample=np.zeros([5, 9])
rewardExample[3,3]=10
rewardExample[3,5]=-100

actionsExample=["up","bottom", "left", "right"]

MazeExample=POMDP(grille, actionsExample, rewardExample,makeTransitionFunctionS(),makeObservationFunctionS())

print(MazeExample.getStates())
print(MazeExample.getActions())
print(MazeExample.getObservationF((3,7)))

print(MazeExample.getTransitionF("up",(3,7)))
