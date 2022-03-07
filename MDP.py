# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:44:29 2022

@author: Sioban
"""

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






def valueIteration(states, reward, actions, wall,  gamma, epsilon):
    delta=math.inf
    U=[]
    Up=[]
    for i in range(len(states)):
        U.append(0)
        Up.append(0)
    iterationN=0
    
    while delta > (epsilon*(1-gamma)/gamma) :
        U=Up.copy()
        delta=0
        
        
        for i in range(len(states)):
            state=states[i]
            "récompense immédiate"
            Up[i]=reward[i]
            t=[]
            for j in range(len(actions)):
                t.append(0)
                
            if(i!=9 and i!=10):
                
        
                stateup=(state[0], state[1]+1)
                stateleft=(state[0]-1, state[1])
                stateright=(state[0]+1, state[1])
                statebottom=(state[0], state[1]-1)
            
                "cas des états terminaux"
            
                
                "calcul pour up"
                "dans le cas ou le deplacement peut s'effectuer"
                if stateup in states:
                    t[0]+=0.8*U[states.index(stateup)]
            
                if stateleft in states:
                    t[0]+=0.1*U[states.index(stateleft)]
                if stateright in states:
                    t[0]+=0.1*U[states.index(stateright)]
                "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateup in wall:
                    t[0]+=0.8*U[i]
                if stateleft in wall:
                    t[0]+=0.1*U[i]
                if stateright in wall:
                    t[0]+=0.1*U[i]
            
                "calcul pour left"
                "dans le cas ou le déplacement peut s'effectuer"
        
                if stateleft in states:
                    t[2]+=0.8*U[states.index(stateleft)]
                if stateup in states:
                    t[2]+=0.1*U[states.index(stateup)]
                if statebottom in states:
                    t[2]+=0.1*U[states.index(statebottom)]
                    "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateleft in wall:
                    t[2]+=0.8*U[i]
                if stateup in wall:
                    t[2]+=0.1*U[i]
                if statebottom in wall:
                    t[2]+=0.1*U[i]
        
                "calcul pour right"
                "dans le cas ou le déplacement peut s'effectuer"
        
                if stateright in states:
                    t[3]+=0.8*U[states.index(stateright)]
                if stateup in states:
                    t[3]+=0.1*U[states.index(stateup)]
                if statebottom in states:
                    t[3]+=0.1*U[states.index(statebottom)]
                    "dans le cas ou le déplacement ne peut pas s'effectuer"
                if stateright in wall:
                    t[3]+=0.8*U[i]
                if stateup in wall:
                    t[3]+=0.1*U[i]
                if statebottom in wall:
                    t[3]+=0.1*U[i]
    
    
                "calcul pour bottom"
                "dans le cas ou le deplacement peut s'effectuer"
                if statebottom in states:
                    t[1]+=0.8*U[states.index(statebottom)]
                if stateleft in states:
                    t[1]+=0.1*U[states.index(stateleft)]
                if stateright in states:
                    t[1]+=0.1*U[states.index(stateright)]
                "dans le cas ou le déplacement ne peut pas s'effectuer"
                if statebottom in wall:
                    t[1]+=0.8*U[i]
                if stateleft in wall:
                    t[1]+=0.1*U[i]
                if stateright in wall:
                    t[1]+=0.1*U[i]
                
                
            maxi=max(t)
            
            Up[i]+=gamma*maxi
        
         
            
            if abs(Up[i]-U[i])>delta:
                delta=abs(Up[i]-U[i])
                
        print(Up)
        print(iterationN)
        iterationN+=1
    
    return U,iterationN

#parameters
c=0.0001
gamma=0.99
c2=0.01
gamma2=0.55


#print(valueIteration(t1, t2, t3,t4, gamma, c))




def transitionFunction(statesArray, state, action):
    #retourne un tableau avec les probabilité associé à chaque état
    t=[]
    for i in range(len(statesArray)):
        t.append(0)
    
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
            t[statesArray.index(stateup)]+=0.8
        else:
            t[statesArray.index(state)]+=0.8
        if stateleft in statesArray:
            t[statesArray.index(stateleft)]+=0.1
        else:
            t[statesArray.index(state)]+=0.1
        if stateright in statesArray:
            t[statesArray.index(stateright)]+=0.1
        else:
            t[statesArray.index(state)]+=0.1
        
        "action left and not a terminal state"
    if action=="left":
         if stateleft in statesArray:
            t[statesArray.index(stateleft)]+=0.8
         else:
            t[statesArray.index(state)]+=0.8
         if stateup in statesArray:
            t[statesArray.index(stateup)]+=0.1
         else:
            t[ statesArray.index(state)]+=0.1
         if statebottom in statesArray:
            t[statesArray.index(statebottom)]+=0.1
         else:
            t[statesArray.index(state)]+=0.1
            
            
    "action right and not a terminal state"
    if action=="right":
         if stateright in statesArray:
            t[statesArray.index(stateright)]+=0.8
         else:
            t[ statesArray.index(state)]+=0.8
         if stateup in statesArray:
            t[statesArray.index(stateup)]+=0.1
         else:
            t[ statesArray.index(state)]+=0.1
         if statebottom in statesArray:
            t[statesArray.index(statebottom)]+=0.1
         else:
            t[statesArray.index(state)]+=0.1
    
    "action bottom and not a terminal state"
    if action=="bottom":
         if statebottom in statesArray:
            t[statesArray.index(statebottom)]+=0.8
         else:
            t[ statesArray.index(state)]+=0.8
         if stateleft in statesArray:
            t[statesArray.index(stateleft)]+=0.1
         else:
            t[ statesArray.index(state)]+=0.1
         if stateright in statesArray:
            t[statesArray.index(stateright)]+=0.1
         else:
            t[statesArray.index(state)]+=0.1
    return t;
    





def valueIterationv2(states, reward, actions, gamma, epsilon):
    delta=math.inf
    U=[]
    Up=[]
    for j in range(len(states)):
        U.append(0)
        Up.append(0)
    iterationN=0
    
    while delta > (epsilon*(1-gamma)/gamma) :
        U=Up.copy()
        delta=0
        
        
        for i in range(len(states)):
            state=states[i]
            "récompense immédiate"
            Up[i]=reward[i]
            
            
            t=[]
            
            for k1 in range(len(actions)):
                t.append(0)
                
                probabilityArray=transitionFunction(states,state,actions[k1])
                for k2 in range(len(states)):
                  
                    t[k1]+=probabilityArray[k2]*U[k2]
            
            

            maxi=max(t)
           
            Up[i]+=gamma*maxi
        
            
           
            if abs(Up[i]-U[i])>delta:
                delta=abs(Up[i]-U[i])
        print(Up)
            
        print(iterationN)        
        iterationN+=1
    
    return U,iterationN

#print(valueIterationv2(t1, t2, t3, gamma, c))


def randomPolicy(states, actions):
    policy=[]
    for i in range(len(states)):
        v=random.randint(0,3)
        action=actions[v]
        policy.append(action)
    return policy

"""def policyEvaluation(pi, U, t1,t2, gamma):
    Up=np.zeros((1,11))
    for i in range(len(t1)):
        value=0
        Up[0,i]=t2[i]
        probabilityArray=transitionFunction(t1,t1[i],pi[i])
        for k in range(len(t1)):
            value+=probabilityArray[0,k]*U[0,k]
        Up[0,i]+=gamma*value
    return Up"""

        

def policyEvaluation(states,reward,gamma,epsilon, pi):
    delta=math.inf
   # U=np.zeros((1,11))
    U=[]
    Up=[]
    #Up=np.zeros((1,11))
    for i in range(len(states)):
        U.append(0)
        Up.append(0)
    iterationN=0
    while delta > (epsilon*(1-gamma)/gamma) :
        U=Up.copy()
        delta=0
        
        
        for i in range(len(states)):
            state=states[i]
            "récompense immédiate"
            Up[i]=reward[i]
            probabilityArray=transitionFunction(states,state,pi[i])
            value=0
            for k1 in range(len(states)):
                value+=probabilityArray[k1]*U[k1]
            Up[i]+=gamma*value
            if abs(Up[i]-U[i])>delta:
                delta=abs(Up[i]-U[i])
        print(Up)
            
        print(iterationN)        
        iterationN+=1
    
    return U

    
print(policyEvaluation(t1,t2,gamma,c, randomPolicy(t1, t3)))

def policyIteration(states, reward,actions, gamma, epsilon):
   
    U=[]
  
    pi=randomPolicy(states, actions)
    unchanged=False
    while not (unchanged):
        Up=(policyEvaluation(states,reward, gamma, epsilon, pi))
        U=Up.copy()
        print(U)
        print(pi)
        unchanged=True
        for i in range(len(states)):
            state=states[i]
            t=[]
            for j in range(len(actions)):
                t.append(0)
            
                
                probabilityArray=transitionFunction(states,state,actions[j])
                for k1 in range(len(states)):
                    
                    t[j]+=probabilityArray[k1]*U[k1]
            maxi=max(t)
            indice=t.index(maxi)
            print(indice)
            
            for k2 in range(len(states)):
                value=0
                probabilityArrayPi=transitionFunction(states, state, pi[i])
                for k3 in range(len(states)):
                    value+=probabilityArrayPi[k3]*U[k3]
            if value<maxi:
                pi[i]=actions[indice]
                unchanged=False
    return pi

print(policyIteration(t1, t2,t3, gamma,c))
print(valueIterationv2(t1, t2, t3, gamma, c))
            
                
            
 
            
            
 