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
reward[3,3]=1
reward[3,5]=-1
print(reward)
