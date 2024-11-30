# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:15:53 2024

@author: barba
"""
import numpy as np
import random


def term_state(A):
    """
    takes in a matrix and says if it is terminal
    """
    win=0
    #checks for column wins
    for i in range(7):
        c1 = np.all(A[:4,i]==np.ones(4)) or np.all(A[:4,i]==2*np.ones(4))
        c2 = np.all(A[1:5,i]==np.ones(4)) or np.all(A[1:5,i]==2*np.ones(4))
        c3 = np.all(A[2:6,i]==np.ones(4)) or np.all(A[2:6,i]==2*np.ones(4))
        win = int(c1 or c2 or c3)
        if win == 1:
            #print("column")
            return win
        
    #checks for row wins
    for i in range(6):
        
        c1 = np.all(A[i,:4]==np.ones(4)) or np.all(A[i,:4]==2*np.ones(4))
        c2 = np.all(A[i,1:5]==np.ones(4)) or np.all(A[i,1:5]==2*np.ones(4))
        c3 = np.all(A[i,2:6]==np.ones(4)) or np.all(A[i,2:6]==2*np.ones(4))
        c4 = np.all(A[i,3:7]==np.ones(4)) or np.all(A[i,3:7]==2*np.ones(4))
        win = int(c1 or c2 or c3 or c4)
        if win == 1:
            #print("row")
            return win    
        
    diags=[np.diag(A,i) for i  in range(-2,4)]
    antidiags = [np.diag(np.fliplr(A),i) for i  in range(-2,4)]
    
    #check for diagonal win
    for d in diags:
        w1=([2,2,2,2] in [list(d[0+i:4+i]) for i in range(3)])
        w2 =([1,1,1,1] in [list(d[0+i:4+i]) for i in range(3)])
        win = int(w1 or w2) 
        if win ==1:
            #print("diag")
            return win
        
    #antidiagonal win
    for d in antidiags:
        w1=([2,2,2,2] in [list(d[0+i:4+i]) for i in range(3)])
        w2 =([1,1,1,1] in [list(d[0+i:4+i]) for i in range(3)])
        win = int(w1 or w2) 
        if win ==1:
            #print("antidiag")
            return win    
    
    if win==0:
        if not np.all(A>0):
            win=-1

    return win

    


# Create a 6x7 matrix with random entries from 0, 1, and 2
rows, cols = 6, 7
A = np.array([[random.choice([0, 1, 2]) for _ in range(cols)] for _ in range(rows)])
term_state(A)



