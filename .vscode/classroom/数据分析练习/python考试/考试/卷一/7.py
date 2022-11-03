# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:52:47 2022

@author: angus

编写python程序对产品销量与广告进行多元线性回归分析，将
目标数据集按比例6：4分割训练集和测试集，用训练集数据拟合预
测，并与实际数据可视化对比。最后利用均方根误差 RMSE（Root 
Mean Square Error，即预测值与真实值偏差的平方与观测次数 n 
比值的平方根，调用函数sqrt()）计算并输出误差。


"""
import pandas as pd 
from matplotlib import pyplot as plt


