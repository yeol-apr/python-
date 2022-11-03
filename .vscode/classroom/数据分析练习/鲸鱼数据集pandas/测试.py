# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:56:10 2022

@author: angus
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
#读入数据
classdata= pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/Python编程题/7/class.csv')
classdata.head()
#散点图1
classdata.plot.scatter(x='Age',y='Height',s=80,c='g')
#散点图2
plt.figure()
plt.scatter(classdata['Height'], classdata['Weight'],c='b')
plt.xlabel("身高")
plt.ylabel("体重")
plt.show()
#计算相关系数
corr = classdata.corr()
#画热图
plt.figure()
sns.heatmap(corr,annot=True,xticklabels=corr.columns,yticklabels=corr.columns)
plt.show()
#相关系数
corr