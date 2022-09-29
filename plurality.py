#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:20:40 2022

@author: miceland
"""

from Data import data, num_alts
import pandas as pd
import numpy as np

def plurality(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    alt_winner = None
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
        
        
    for i in inds:
        alts[i] = len(data[data.iloc[:, 0] == i])
        
        
        
    alt_winner = alts.max()
    
    return (alts[alts == alt_winner].index[0])

alt_winner = plurality(num_alts, data)


        
