# -*- coding: UTF-8 -*-
"""
# @Time: 2021/9/14 21:13
# @Author: 远方的星
# @CSDN: https://blog.csdn.net/qq_44921056
"""
import turtle as turtle
import math

turtle.hideturtle()
turtle.speed(10)


class MoonCake(object):
    def __init__(self, name: str):
        self.name = name

    #  画月饼的花边
    def external_pattern(self, r: int, n: int):  # r为外部花边的圆的半径；n为外部花边的个数
        turtle.penup()
        turtle.goto(0, -r)
        turtle.pendown()

        round_r = math.sin(math.pi / n) * r  # 月饼花圈的半径

        for i in range(n):
            turtle.penup()  # 画笔抬起
            turtle.home()  # 恢复为初始位置
            turtle.seth((360/n) * i)  # 改变画笔方向，但不前进
            turtle.fd(r)
            turtle.left((360/n) * 0.5)  # 画笔左转一定的角度
            turtle.pendown()
            turtle.color('#F0BE7C')  # 设置颜色
            turtle.begin_fill()  # 开始填充颜色
            turtle.circle(round_r, 180)
            turtle.end_fill()

    # 画内部纹路图案
    def internal_pattern(self):
        turtle.color('#F5E16F')
        turtle.goto(0, -180)
        for _ in range(8):
            turtle.begin_fill()
            turtle.circle(60, 120)
            turtle.left(180)
            turtle.circle(60, 120)
            turtle.end_fill()

    # 画圆的子函数，下文需要调用
    def draw_circle(self, r: int, pensize: int, color1: str, color2: str):
        turtle.penup()
        turtle.goto(0, -r)
        turtle.seth(0)
        turtle.pendown()
        turtle.pensize(pensize, )
        turtle.color(color1, color2)
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    # 画月饼内部的框架的子函数，下文需要调用
    def draw(self):
        turtle.title("楠楠中秋快乐")  # 画板窗口的标题
        self.external_pattern(200, 12)  # 月饼的外花边
        self.draw_circle(200, 10, '#F0BE7C', '#F0BE7C')  # 画上大圆圈
        self.draw_circle(180, 10, '#F8CD32', '#FBA92D')  # 画上小圆圈
        self.internal_pattern()
        self.write_text(-105, -60)
        turtle.done()

    # 填写月饼中间的文本
    def write_text(self, x: float, y: float):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color('Gold')
        turtle.write(self.name, font=("华文隶书", 80, "bold"))  # 写上文本


if __name__ == '__main__':
    MoonCake('五仁').draw()


