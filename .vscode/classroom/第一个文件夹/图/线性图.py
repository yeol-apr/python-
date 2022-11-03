from matplotlib import pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['LiSu']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x = range(11, 31)
a = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
fig = plt.figure(figsize=(18, 10), dpi=60)
plt.plot(x, a, label="同桌",color='r',linestyle='--',linewidth=5)  # 画图标注线,颜色，线条样式，粗细
plt.plot(x, y, label="自己")
_x = [f"{i}岁" for i in x]
plt.xticks(list(x), _x,rotation=45)
plt.xlabel("年龄")
plt.ylabel("男友 单位（个）")
plt.title("年龄和男友的关系")
plt.legend()#给图中的线做标注，括号里面的参数是修改标注图线的位置
plt.grid(alpha=0.4)  # 添加图像网格,alpha是透明度
plt.show()
