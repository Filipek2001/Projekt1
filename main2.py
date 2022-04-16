# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:00:43 2022

@author: filom
"""


import numpy as np
from math import radians
import sys
sys.path.append('C:\\Users\\filom\\OneDrive - Politechnika Warszawska\\Pulpit\\Projekt_infa\\transformacje_wsp')
from transformacje_wsp import *


file = 'wsp_inp.txt'
results = Transformacje(model = "grs80")


board = np.genfromtxt(file, delimiter=',', skip_header = 4)
rows,cols = np.shape(board)

hirvonen = np.zeros((rows,cols))
flh2xyz = np.zeros((rows,cols))
u2000 = np.zeros((rows,2))
u1992 = np.zeros((rows,2))
XYZ2el = np.zeros((rows,2))



for i in range(rows):
    
    hirvonen[i] = results.hirvonen(board[i,0],board[i,1],board[i,2])
    
    flh2xyz[i] = results.flh2xyz(radians(hirvonen[i,0]),radians(hirvonen[i,1]),(hirvonen[i,2]))
    
    u2000[i] = results.u2000(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    
    u1992[i] = results.u1992(radians(hirvonen[i,0]), radians(hirvonen[i,1]))
    
    XYZ2el[i] = results.XYZ2el(board[i,0],board[i,1],board[i,2],radians(hirvonen[i,0]), radians(hirvonen[i,1]),hirvonen[i,2])

 
