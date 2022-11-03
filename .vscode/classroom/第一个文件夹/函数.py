#导入坐标图表。
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,10),dpi=60)
'''figure图形，图标的意思。图D:\下载像模糊的时候传入dip参数，让图片清晰'''

x=range(2,26,2)
y=[15,13,14,17,20,25,26,26,24,22,18,15]
plt.plot(x,y)
'''传入x,y两个坐标图的图像'''
#设置x轴的刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(range(25,50))
plt.xticks(range(min(y),max(y)+1))
plt.savefig("./size.png")
#展示图像
plt.show()