import pandas as pd
#爬取的网络地址 url
url="https://s.askci.com/stock/a/"
#A 股公司营业收入排行榜位于所有表格中的第一个，索引为 0
df=pd.read_html(url)[0]
print(df)
