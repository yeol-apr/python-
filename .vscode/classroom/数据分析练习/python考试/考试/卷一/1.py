# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:04:51 2022

@author: angus
导入（爬取）网络数据，编写一个简易爬虫程序，爬取中商情
报网中 A 股公司营业收入排行榜表格来获取相应的金融数据，网址
为https://s.askci.com/stock/a/。
"""
import pandas as pd
df=pd.read_html('https://s.askci.com/stock/a/')[0]#‘内含网址’，【】内的数子代表在哪里。第几个。
print(df)


