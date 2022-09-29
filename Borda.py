from Data import data, num_alts
import pandas as pd
import numpy as np


def Borda(num_alts, data):
    inds = [i for i in range(1, num_alts + 1)]
    alt_winner = None
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if (pd.isna(data.iloc[i, j])):
                break
            alts[data.iloc[i, j]] += len(data.iloc[i, (j + 1):])
            
    alt_winner = alts.max()

    return alts[alts == alt_winner].index[0]

alt_winner = Borda(num_alts, data)
        