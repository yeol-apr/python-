# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:09:09 2022

@author: angus
请利用python查看sales.csv文件中的数据表的大小，要求返回数
据表中行的个数和列的个数。
"""
import pandas as  pd
df=pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/卷一/Python编程题/2/sales.csv',encoding='gbk')
print(df.shape[0],df.shape[1])



