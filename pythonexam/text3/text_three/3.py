# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:55:44 2022

@author: angus
"""
import pandas as pd
one=pd.DataFrame({
'Name':['Alex','Amy','Allen','Alice','Ayoung'],
'subject_id':['sub1','sub2','sub4','sub6','sub5'],
'Marks_scored':[98,90,87,69,78]},
index=[1,2,3,4,5])

two=pd.DataFrame({
'Name':['Billy','Brian','Bran','Bryce','Betty'],
'subject_id':['sub2','sub4','sub3','sub6','sub5'],
'Marks_scored':[89,80,79,97,88]},
index=[1,2,3,4,5])


three=pd.DataFrame({
'Name':['Alex','Amy','Allen','Alice','Ayoung'],
'subject_id':['sub1','sub2','sub4','sub6','sub5'],
'Marks_scored':[98,90,87,69,78]},
index=[1,2,3,4,5])
print(pd.merge(one, two))
print(one.join(two))      

'''
merge(左，右，on='基于那一列拼接'，how='左连接或者有链接 ')
'''

#print(pd.concat([one,two],keys=['x','y']))
'''
objt=[哈希表或者是dataframe]
默认为纵向（0轴）拼接，横向1轴拼接axis；
参数一在上面。
keys表示将值关联在表的第一行。
ignore_index为true表示不展示行索引和关联zhi。

'''


