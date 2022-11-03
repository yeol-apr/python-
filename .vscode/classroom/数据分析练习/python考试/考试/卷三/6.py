# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:43:47 2022

@author: angus
"""

import pandas as pd
import matplotlib.pyplot as plt
labels = ['A','B','C','D','E']
x = [15,30,30,10,15]
plt.pie(x, labels = labels)
plt.show