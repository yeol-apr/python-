# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:15:02 2022

@author: angus
对于存储在该Python文件同目录下的某电商平台销售数据
product_sales.csv，请利用Python对数据读取，并计算每一行数据的非
空值个数情况。
isnull查看缺失值

"""

import pandas as pd
df=pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/卷一/Python编程题/3/product_sales.csv',encoding='gbk')
print(df.isnull().count())
print(df.count())
