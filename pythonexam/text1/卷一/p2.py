#请利用python查看sales.csv文件中的数据表的大小，要求返回数
#据表中行的个数和列的个数。
import pandas as pd

df = pd.read_csv('C:/Users/13208/Desktop/鲸鱼数据集/pandas_exercise (1)/exercise_data/Apple_stock.csv',encoding='gbk')

print(df.shape[0],df.shape[1])#shape是属性，shape[o]代表行，shape[1]代表列，-1代表最后一个，类推