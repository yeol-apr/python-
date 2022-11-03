from matplotlib import pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['LiSu']
fig = plt.figure(figsize=(15, 8), dpi=80)
a = ['战狼2', '速度与激情8', '功夫瑜伽', '西游']
b = [56.01, 26, 94, 17]
c = [6, 5, 9, 8]
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
"""
绘制水平条形图方法barh
参数一：y轴
参数二：x轴
"""
plt.bar(range(len(a)), b, width=0.2, label='jiahe')  # 方法bar表示绘制条形图
_x = [i + 0.2 for i in range(len(a))]
plt.bar(_x, c, width=0.2, label='py')  # 标注在线上。
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks(range(len(a)), a)
plt.legend()  # 显示备注的标注
plt.xlabel('电影名称')
plt.ylabel('单位 （部）')
plt.title('影院电源查看人数')
plt.savefig('./条形图.png')  # 保存到当前文件文件夹
plt.grid()  # 展示网格图
plt.show()
