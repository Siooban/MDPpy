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
    def getRewardOnState(self, state):
        return self.rewards[state]
    def getObservationF(self, currentState):
        return self.ObservationF(self.states, currentState)
    def getTransitionF(self,action, currentState):
        return self.TransitionF(self.states,action,currentState)
    
    
    
    
    

    
class Simulateur(object):
    def __init__(self, POMDP,initializationF,updateF):
        self.POMDP=POMDP
        self.initializationF=initializationF
        initialization=initializationF(POMDP)
        self.currentState=initialization[0]
        self.belief=initialization[1]
        self.updateF=updateF
      
        
    
        
    def getCurrentState(self):
        return self.currentState
        
    def getBelief(self):
        return self.belief
        
    def displayCurrentState(self):
        print(self.getCurrentState())
        
    def displayBelief(self):
        print(self.getBelief())
        
    def getAllObservationF(self):
        return self.allObservationF(self.POMDP.getStates(), self.currentState)
    
    def updateModel(self,newObservation,action):
        self.belief=self.updateF(self.POMDP, self.belief,newObservation,action)
    
    def makeTransition(self,action):
        possibleTransition=self.POMDP.getTransitionF(action, self.currentState)
        test=[True, True]
        for key in possibleTransition.keys():
            if possibleTransition[key]==0.9:
                test[0]=False
            if possibleTransition[key]==0.2:
                test[1]=False
        chosenTransition=random.randint(1,10)
        if test[0] and test[1]:
            for key in possibleTransition.keys():
                
                if possibleTransition[key]==0.8 and chosenTransition<=8:
                    return key
                if possibleTransition[key]==0.1 and chosenTransition==9:
                    return key
                if possibleTransition[key]==0.1 and chosenTransition==10:
                    return key
        elif test[0]:
            if possibleTransition[key]==0.8 and chosenTransition<=8:
                return key
            if possibleTransition[key]==0.2 and chosenTransition>8:
                return key
        else:
            for key in possibleTransition.keys():
               
                if possibleTransition[key] ==0.9 and chosenTransition<=9:
                    return key
                if possibleTransition[key]==0.1 and chosenTransition==10:
                    return key
            
                
        
                
                
                
        
        
    def runSimu(self):
        print(self. belief)
        while True:
            
            action=input("action choice: up, bottom, right, left")
            print(action)
            
            possibleCurrentState=self.POMDP.getTransitionF(action, self.currentState)
            print(possibleCurrentState)
            self.currentState=self.makeTransition(action)
            print(self.currentState)
            key_list = list(possibleCurrentState.keys())
            print(key_list)
            
                
            allOb=self.POMDP.getObservationF(self.currentState)
            observationArray=allOb[0]
            if allOb[2]==1:
                currentOb=observationArray[1]
            elif allOb[2]==2:
                currentOb=observationArray[2]
            elif allOb[2]==3:
                currentOb=observationArray[3]
            elif allOb[2]==4:
                currentOb=observationArray[4]
            else:
                currentOb=observationArray[0]
                
            self.updateModel(currentOb,action)
            print(self.belief)
        
            if self.POMDP.getRewardOnState(self.currentState)==10:
                print("Victory")
                return 
            if self.POMDP.getRewardOnState(self.currentState)==-100:
                print("Defeat")
                return 
        
        
def makeInitFunction():
    def initialize(POMDP):
        states=POMDP.getStates()
        shape=np.shape(states)
        t=[]
        result=np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                if states[i,j]==1:
                    t.append((i, j))
        value=random.randint(0, len(t)-1)
        result[t[value]]=1       
        return  t[value], result
    return initialize
    
def makeUpdateFunction():
    def updateFunction(POMDP, oldBelief, newObservation, action):
        shape=np.shape(POMDP.getStates())
        """ new observation is an observation followed by the probability for this 
        observation to occur"""
        result=np.zeros(shape)
        """alpha is the normalisation factor"""
        alpha=0
        
        """ for all states"""
        for i in range(shape[0]):
            for j in range(shape[1]):
                
                if oldBelief[i,j]:
                    newPossiblePosition=POMDP.getTransitionF(action, (i,j))
                    for key in newPossiblePosition:
                        testObservations=POMDP.getObservationF(key)
                        possibleObservation=testObservations[0]
                        observationProba=testObservations[1]
                        for k in range(len(possibleObservation)):
                            if compare(possibleObservation[k],newObservation):
                                value=newPossiblePosition[key]*oldBelief[i,j]*observationProba[k]
                                result[key]+=value
                                alpha+=value
        """ normalization"""
        for i in range(shape[0]):
            for j in range(shape[1]):
                result[i,j]/=alpha
        return result
    return updateFunction
        
def compare(obs1, obs2):
    for i in range(len(obs1)):
        if obs1[i]!=obs2[i]:
            return False
    return True


        

    
""" this version return the an array that contain two possibility with their probability""" 
def makeObservationFunctionS():
        
    """ this function return the wall number surrounding a position
    with uncertainty """
    def ObservationFunctionS(states, currentState):
        """normal observation"""
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
        """ other observation"""
        for i in range(0,4):
            value=wallDistribution.copy()
            if value[i]:
                value[i]=False
            else:
                value[i]=True
            wallDistributions.append(value)
            proba.append(0.05)
        chosenValue=random.randint(1,20)
        return wallDistributions, proba, chosenValue
    return ObservationFunctionS



"""return a simple observation with uncertainty"""
def makeObservationFunctionSv2():
        
    """ this function return the wall number surrounding a position
    with uncertainty """
    def ObservationFunctionSv2(states, currentState):
        
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
        
        """ uncertainty"""
        value=random.randint(0,3)
        if wallDistribution[value]==False:
            wallDistribution[value]=True
        else:
            wallDistribution[value]=False
        wallDistributions.append(wallDistribution)
        
        ObservationChosen=random.randint(1,10)
        if ObservationChosen>8:
            return wallDistributions[1]
        else:
            return wallDistribution[0]
    
    return ObservationFunctionSv2

    
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
testSimu=Simulateur(MazeExample, makeInitFunction(),makeUpdateFunction())
print(MazeExample.getStates())
print(MazeExample.getActions())
print(MazeExample.getObservationF((3,7)))

#testSimu.displayCurrentState()
#testSimu.displayBelief()
testSimu.runSimu()


#print(MazeExample.getTransitionF("up",(3,7)))
