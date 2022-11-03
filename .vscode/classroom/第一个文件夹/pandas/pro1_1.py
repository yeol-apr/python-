import pandas as pd

# 读入 sales.xlsx 文件的前十行
df = pd.read_excel("Desktop/Python 数据集/sales.xlsx")
df1 = df.head(10)
# 读入 sales.xlsx 文件的后五行
df2 = df.tail(5)
# 打开 sales_new.xlsx 文件
work = pd.ExcelWriter('sales_new.xlsx')
