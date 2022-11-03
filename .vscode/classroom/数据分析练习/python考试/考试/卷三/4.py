# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:00:33 2022

@author: angus
"""

import pandas as pd
tips= pd.read_csv('C:/Users/13208/Desktop/BBDA数据分析/试题文件/Python编程题/4/tips.csv',encoding=('gbk'))
result=pd.pivot_table(tips,index=['day','smoker'])
print(result)


'''


'''