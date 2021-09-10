# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:29:56 2021

@author: 123
"""
import random
users={'calvo':'santiago6244@gmail.com','lata':'tatianapulgarin@gmail.com','juan':'juanito@gmail.com'}
sel={}
l=list(users.items())
def rand1(x):   
    ran1=random.choice(x)
    return ran1
def rand2(y):   
    ran2= random.choice(y)
    return ran2
    
def corr(ran1,ran2,sel):
    
    while ran1[0]==ran2[0]:
       rand1(l)
       rand2(l)
       print('oe')
    sel[ran1[0]]=ran2[0]
t=0    
for i in range(len(l)):
    t=t+i
    corr(rand1(l),rand2(l),sel)
    if len(sel)!= len(users):
        sel={}
        corr(rand1(l),rand2(l),sel)    
print(sel,t)
    
    
       