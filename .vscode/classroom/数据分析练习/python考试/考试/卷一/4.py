# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:20:53 2022

@author: angus
读取数据集，添加了一个小费百分比的列tip_pct，按‘smok
e’分组并运用apply（）函数选出最高的5个tip_pct值，为防止分
组键跟原始对象的索引共同构成结果对象中的层次化索引，需要设
置禁止分组键
"""
import pandas as pd
df=pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/卷一/Python编程题/4/tips1.csv',encoding='gbk')
df.info()
df.groupby('smoker')
df.apply()
