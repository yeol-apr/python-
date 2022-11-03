# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:45:47 2022

@author: angus
"""
import pandas as pd
df=pd.DataFrame({'item1':[None,2,3,4,None],'item2':[1,2,None,4,5],
                 'item3':[1,2,3,4,None],'item4':[1,2,None,None,5],
                 'item5':[1,2,3,None,None],'item6':[None,2,None,4,None]})
df['item2'].interpolate(method='spline',order=3)