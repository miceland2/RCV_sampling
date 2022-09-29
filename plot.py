#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:57:22 2022

@author: miceland
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

samples = pd.read_csv('pluralities.txt', names=[i*10 for i in range(1, 11)])
samples.columns = [i*10 for i in range(1, 11)]

mean = samples.mean()

x = samples.columns
y = mean

model = np.poly1d(np.polyfit(x, y, 4))
polyline = np.linspace(1, 100, 100)

plt.scatter(x, y)
plt.plot(polyline, model(polyline), color='orange')



plt.title("Prediction Accuracy v. Sample Size")
plt.xlabel("Sample size percentage")
plt.ylabel("Percent accuracy")


plt.show()