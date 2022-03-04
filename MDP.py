# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:44:29 2022

@author: Sioban
"""
import numpy as np
import random
import math
"states array"
t1=[(1,1),(1,2),(1,3),(2,1),(2, 3),(3,1),(3,2),(3,3),(4, 1),(4, 2),(4, 3)]

"states value"
t2=[-0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -0.04, -1, 1]
"actions"
t3=["up", "bottom", "left", "right"]
"wall array"
t4=[(0, 1), (0, 2),(0,3), (2, 2),(1,0), (2,0),(3,0), (4,0),(5,1),(5,2),(5,3),(1,4),(2,4),(3,4),(4,4)]

U=np.zeros((1,11))




def valueIteration(t1, t2, t3, gamma, epsilon):
    delta=math.inf
    U=np.zeros((1,11))
    Up=np.zeros((1,11))
    iterationN=0
    
    while delta > (epsilon*(1-gamma)/gamma) :
        U=np.copy(Up)
        delta=0
        
        
        for i in range(len(t1)):
            state=t1[i]
            "récompense immédiate"
            Up[0,i]=t2[i]
            
            t=np.zeros((1, 4))
            if(i!=9 and i!=10):
                
        
                stateup=(state[0], state[1]+1)
                stateleft=(state[0]-1, state[1])
                stateright=(state[0]+1, state[1])
                statebottom=(state[0], state[1]-1)
            
                "cas des états terminaux"
            
                
                "calcul pour up"
                "dans le cas ou le deplacement peut s'effectuer"
                if stateup in t1:
                    t[0,0]+=0.8*U[0,t1.index(stateup)]
            
                if stateleft in t1:
                    t[0,0]+=0.1*U[0,t1.index(stateleft)]
                if stateright in t1:
                    t[0,0]+=0.1*U[0,t1.index(stateright)]
                "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateup in t4:
                    t[0,0]+=0.8*U[0,i]
                if stateleft in t4:
                    t[0,0]+=0.1*U[0,i]
                if stateright in t4:
                    t[0,0]+=0.1*U[0,i]
            
                "calcul pour left"
                "dans le cas ou le déplacement peut s'effectuer"
        
                if stateleft in t1:
                    t[0,2]+=0.8*U[0,t1.index(stateleft)]
                if stateup in t1:
                    t[0,2]+=0.1*U[0,t1.index(stateup)]
                if statebottom in t1:
                    t[0,2]+=0.1*U[0,t1.index(statebottom)]
                    "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateleft in t4:
                    t[0,2]+=0.8*U[0,i]
                if stateup in t4:
                    t[0,2]+=0.1*U[0,i]
                if statebottom in t4:
                    t[0,2]+=0.1*U[0,i]
        
                "calcul pour right"
                "dans le cas ou le déplacement peut s'effectuer"
        
                if stateright in t1:
                    t[0,3]+=0.8*U[0,t1.index(stateright)]
                if stateup in t1:
                    t[0,3]+=0.1*U[0,t1.index(stateup)]
                if statebottom in t1:
                    t[0,3]+=0.1*U[0,t1.index(statebottom)]
                    "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateright in t4:
                    t[0,3]+=0.8*U[0,i]
                if stateup in t4:
                    t[0,3]+=0.1*U[0,i]
                if statebottom in t4:
                    t[0,3]+=0.1*U[0,i]
    
    
                "calcul pour bottom"
                "dans le cas ou le deplacement peut s'effectuer"
                if statebottom in t1:
                    t[0,1]+=0.8*U[0,t1.index(statebottom)]
                if stateleft in t1:
                    t[0,1]+=0.1*U[0,t1.index(stateleft)]
                if stateright in t1:
                    t[0,1]+=0.1*U[0,t1.index(stateright)]
                "dans le cas ou le déplacement ne peut pas s'effectuer"
                if statebottom in t4:
                    t[0,1]+=0.8*U[0,i]
                if stateleft in t4:
                    t[0,1]+=0.1*U[0,i]
                if stateright in t4:
                    t[0,1]+=0.1*U[0,i]
                
                
            maxi=np.max(t)
            #print(maxi)
            Up[0,i]+=gamma*maxi
        
         
            #print(abs(Up[0,i]-U[0,i]))
            #print(Up[0,i])
            #print(U[0,i])
            if abs(Up[0,i]-U[0,i])>delta:
                delta=abs(Up[0,i]-U[0,i])
                
        print(Up)
        print(iterationN)
        iterationN+=1
    
    return U,iterationN
#parameters
c=0.0001
gamma=0.99
c2=0.01
gamma2=0.55


print(valueIteration(t1, t2, t3, gamma, c))


def transitionFunction(statesArray, state, action):
    #retourne un tableau avec les probabilité associé à chaque état
    t=np.zeros((1,11))
    
    
    stateup=(state[0], state[1]+1)
    stateleft=(state[0]-1, state[1])
    stateright=(state[0]+1, state[1])
    statebottom=(state[0], state[1]-1)
    "terminal states"
    if (state==(4,3)):
        return t;
    if (state==(4,2)): 
        return t;
    
    "action up and not a terminal state"
    if action=="up":
        if stateup in statesArray:
            t[0,statesArray.index(stateup)]+=0.8
        else:
            t[0, statesArray.index(state)]+=0.8
        if stateleft in statesArray:
            t[0,statesArray.index(stateleft)]+=0.1
        else:
            t[0, statesArray.index(state)]+=0.1
        if stateright in statesArray:
            t[0,statesArray.index(stateright)]+=0.1
        else:
            t[0,statesArray.index(state)]+=0.1
        
        "action left and not a terminal state"
    if action=="left":
         if stateleft in statesArray:
            t[0,statesArray.index(stateleft)]+=0.8
         else:
            t[0, statesArray.index(state)]+=0.8
         if stateup in statesArray:
            t[0,statesArray.index(stateup)]+=0.1
         else:
            t[0, statesArray.index(state)]+=0.1
         if statebottom in statesArray:
            t[0,statesArray.index(statebottom)]+=0.1
         else:
            t[0,statesArray.index(state)]+=0.1
            
            
    "action right and not a terminal state"
    if action=="right":
         if stateright in statesArray:
            t[0,statesArray.index(stateright)]+=0.8
         else:
            t[0, statesArray.index(state)]+=0.8
         if stateup in statesArray:
            t[0,statesArray.index(stateup)]+=0.1
         else:
            t[0, statesArray.index(state)]+=0.1
         if statebottom in statesArray:
            t[0,statesArray.index(statebottom)]+=0.1
         else:
            t[0,statesArray.index(state)]+=0.1
    
    "action bottom and not a terminal state"
    if action=="bottom":
         if statebottom in statesArray:
            t[0,statesArray.index(statebottom)]+=0.8
         else:
            t[0, statesArray.index(state)]+=0.8
         if stateleft in statesArray:
            t[0,statesArray.index(stateleft)]+=0.1
         else:
            t[0, statesArray.index(state)]+=0.1
         if stateright in statesArray:
            t[0,statesArray.index(stateright)]+=0.1
         else:
            t[0,statesArray.index(state)]+=0.1
    return t;
    
print(transitionFunction(t1, (4,3), "up"))
print(transitionFunction(t1, (3,1), "bottom"))




def valueIterationv2(t1, t2, t3, gamma, epsilon):
    delta=math.inf
    U=np.zeros((1,11))
    Up=np.zeros((1,11))
    iterationN=0
    
    while delta > (epsilon*(1-gamma)/gamma) :
        U=np.copy(Up)
        delta=0
        
        
        for i in range(len(t1)):
            state=t1[i]
            "récompense immédiate"
            Up[0,i]=t2[i]
            
            t=np.zeros((1, 4))
            for action in t3:
                
                probabilityArray=transitionFunction(t1,state,action)
                for k1 in range(len(t1)):
                    t[0,t3.index(action)]+=probabilityArray[0,k1]*U[0,k1]
            
            

            maxi=np.max(t)
           # print(maxi)
            Up[0,i]+=gamma*maxi
        
            
            #print(abs(Up[0,i]-U[0,i]))
            #print(Up[0,i])
            #print(U[0,i])
            if abs(Up[0,i]-U[0,i])>delta:
                delta=abs(Up[0,i]-U[0,i])
        print(Up)
            
        print(iterationN)        
        iterationN+=1
    
    return U,iterationN

print(valueIterationv2(t1, t2, t3, gamma, c))


def randomPolicy(t1, t3):
    policy=[]
    for i in range(len(t1)):
        v=random.randint(0,3)
        action=t3[v]
        policy.append(action)
    return policy

def policyEvaluation(pi, U, t1,t2, gamma):
    Up=np.zeros((1,11))
    for i in range(len(t1)):
        value=0
        Up[0,i]=t2[i]
        probabilityArray=transitionFunction(t1,t1[i],pi[i])
        for k in range(len(t1)):
            value+=probabilityArray[0,k]*U[0,k]
        Up[0,i]+=gamma*value
    return Up

        

"""def policyEvaluation(t1,t2,t3,gamma,epsilon, pi):
    delta=math.inf
    U=np.zeros((1,11))
    Up=np.zeros((1,11))
    iterationN=0
    while delta > (epsilon*(1-gamma)/gamma) :
        U=np.copy(Up)
        delta=0
        
        
        for i in range(len(t1)):
            state=t1[i]
            "récompense immédiate"
            Up[0,i]=t2[i]
            probabilityArray=transitionFunction(t1,state,pi[i])
            value=0
            for k1 in range(len(t1)):
                value+=probabilityArray[0,k1]*U[0,k1]
            Up[0,i]+=gamma*value
            if abs(Up[0,i]-U[0,i])>delta:
                delta=abs(Up[0,i]-U[0,i])
        print(Up)
            
        print(iterationN)        
        iterationN+=1
    
    return U,iterationN
"""
    
#print(policyEvaluation(t1,t2,t3,gamma,c, randomPolicy(t1, t3)))

def policyIteration(t1, t2,t3, gamma):
    U=np.zeros((1,11))
    pi=randomPolicy(t1, t3)
    unchanged=False
    while not (unchanged):
        Up=(policyEvaluation(pi,U,t1,t2,gamma))
        U=np.copy(Up)
        print(U)
        print(pi)
        unchanged=True
        for i in range(len(t1)):
            state=t1[i]
            t=[0,0,0,0]
            for action in t3:
                
                probabilityArray=transitionFunction(t1,state,action)
                for k1 in range(len(t1)):
                    t[t3.index(action)]+=probabilityArray[0,k1]*U[0,k1]
            maxi=np.max(t)
            indice=t.index(maxi)
            print(indice)
            
            for k2 in range(len(t1)):
                value=0
                probabilityArrayPi=transitionFunction(t1, state, pi[i])
                for k3 in range(len(t1)):
                    value+=probabilityArrayPi[0,k3]*U[0,k3]
            if value<maxi:
                pi[i]=t3[indice]
                unchanged=False
    return pi

print(policyIteration(t1, t2,t3, gamma))
print(valueIterationv2(t1, t2, t3, gamma, c))
            
                
            
 
            
            
 