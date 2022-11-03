import matplotlib.pyplot as plt
data=[12.23, 12.59, 12.36, 12.47, 12.85, 12.79, 12.76]
date=[' 12/31/2021',' 04/01/2022' ,'05/01/2022' ,'06/01/2022' ,'07/01/2022' ,'10/01/2022' ,'11/01/2022' ]
plt.figure (figsize=(7, 4))
plt.plot(date, data,'b',label='stock xxxxxx')#r是红色
plt.plot(date,data,'ro')#ro是红色空心圆
plt. grid (True)#网格线
plt. legend(loc=0)
plt. xlabel('日期')
plt. ylabel('收盘价')
plt. title('close price of stock xxxxxx')
plt. savefig('test',dpi=60)
plt.show()