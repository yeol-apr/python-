#对于存储在该Python文件同目录下的某电商平台销售数据
#product_sales.csv，请利用Python对数据读取，并计算每一行数据的非
#空值个数情况
import pandas as pd

df = pd.read_csv('C:/Users/13208/Desktop/鲸鱼数据集/pandas_exercise (1)/exercise_data/Apple_stock.csv',encoding='gbk')
print(df.count(axis=1))