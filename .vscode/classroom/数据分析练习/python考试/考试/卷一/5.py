# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:25:51 2022

@author: angus
时间序列分析，对于给定的股票交易数据，请利用自回归滑动
平均（ARMA）模型进行数据拟合，输出ARMA模型的拟合效果
图。
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
IndexData = pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/卷一/Python编程题/5/timeseries_data.csv',encoding='gbk')
data = IndexData['close' ]
temp = np.array (data)
for q in range(10) :
    try:
        
        model=sm.tsa.ARMA(temp,order=(3, q)) 
        results_ARMA=model.fit()
    except :
        pass
plt.figure(figsize=(10, 4))
plt.plot(temp,'b',label=' close' )
plt.plot(results_ARMA.fittedvalues,' r',label='ARMA model' )
plt.legend()

