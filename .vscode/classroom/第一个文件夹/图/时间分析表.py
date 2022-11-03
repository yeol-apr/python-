from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


x = range(0,120)
y=[random.randint(20,35) for i in range(120)]
fig = plt.figure(figsize=(10,10),dpi=60)
plt.plot(x,y)
_xtick_labels = [f"10:{i}分" for i in range(60)]
_xtick_labels += [f"11h:{i}''" for i in range(60)]#格式化输出。
plt.rcParams['font.sans-serif']=['LiSu'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xlabel("时间")#x坐标轴表示什么
plt.ylabel("温度 单位(℃)")#y坐标轴表示什么
plt.title("10点到12点的温度变化")#整个图片的信息
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)#rotation是对于x轴输出的值做一个逆时针旋转
plt.show()