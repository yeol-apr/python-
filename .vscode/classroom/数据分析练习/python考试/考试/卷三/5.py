# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:47:04 2022

@author: angus
"""

import datetime 
str = '2022-08-28 00:00:00'
str = datetime.datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
str1 = str.strftime("%Y-%m-%d %H:%M:%S")
print(str1,type(str1))