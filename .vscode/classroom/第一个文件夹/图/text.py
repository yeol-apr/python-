import turtle as t


def fu(x, y,z):
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.setheading(z)
    for i in range(5):
        t.forward(40)
        t.right(144)
    t.end_fill()


if __name__ == '__main__':
    t.setup(width=1200, height=600)
    t.screensize(bg='red')  # 设置背景颜色

    # 设置五角星，主
    t.penup()
    t.goto(-550, 150)
    t.seth(0)
    t.pendown()

    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(120)
        t.right(144)
    t.end_fill()
    fu(-400,200,45)
    fu(-360,130,-15)
    fu(-360,60,330)
    fu(-400,-10,330)

'''
t.fillcolor('yellow')
t.begin_fill()
t.speed(1)
for i in range(5):
    t.speed(250)
    t.forward(30)
    t.left(72)
    t.forward(30)
    t.right(144)
t.end_fill()
'''


t.done()
