# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:21:28 2022

@author: angus
"""

def sum_max(arr):
    maxSum=0#记录子序列和的最大数
    
    max_zu=[]
    for i in range(len(arr)):
        print(i)
        curSum=0
        max_zu_zi=[]
        for j in range(i,len(arr)):
            print('j=',j)
            curSum+=arr[j]
            max_zu_zi.append(a[j])
            print('curSum',curSum)
            if curSum>maxSum:
                maxSum=curSum
                print('maxSum',maxSum)
                max_zu=i#最大子序列的开始
                print('max_zu==',max_zu)    
              

    

        print(max_zu_zi)     
    return maxSum,print(max_zu)

a=[-2,11,-4,13,-5,-3]
print('----',sum_max(a))
