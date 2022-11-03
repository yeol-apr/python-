b=[31,28,31,30,31,30,31,31,30,31,30,31]
c=[31,29,31,30,31,30,31,31,30,31,30,31]
year=int(input('输入年份'))
if year // 4 ==0 and  year /100 != 0 or year / 400==0:
    print('闰年')
    a=int(input('请输入月份'))
    if a>0 and a<13:
        print(f"这个月有{c[a-1]}天")
else:
    print('不是闰年')
    a=int(input('请输入月份'))
    if a>0 and a<13:
        print(f"这个月有{b[a-1]}天")

