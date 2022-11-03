import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['LiSu']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

cars = pd.read_csv("C:/Users/13208/Desktop/鲸鱼数据集/pandas_exercise (1)/exercise_data/second_cars_info.csv", encoding='gbk')
fig = plt.figure(figsize=(20, 8), dpi=60)

print(cars.head(10))
# print(apple_s['High'].head(10),'#'*10,apple_s['High'].tail(10))
x1 = cars['Boarding_time'].head(10)

x = cars['Km'].head(10)
y = cars['Sec_price'].head(10)
plt.plot(x, y, label='公里', color='r', linestyle='--', linewidth=3)
plt.plot(x1, y, label='上牌时间')
plt.xlabel("公里数")  # x坐标轴表示什么
plt.ylabel("价格")  # y坐标轴表示什么
plt.title("价格和公里数的关系")  # 整个图片的信息
plt.grid()
plt.show()
