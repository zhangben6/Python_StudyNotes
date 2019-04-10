# 练习:
#    1. 输入一个圆的半径,打印出这个圆的面积

#    2. 输入一个圆的面积,打印出这个圆的半径
#        (要求用math模块内的函数和数据)


import math

# 1. 输入一个圆的半径,打印出这个圆的面积
r1 = float(input("请输入半径: "))
area1 = math.pi * r1 ** 2
print("半径为", r1, '的圆的面积是:', area1)

# 2. 输入一个圆的面积,打印出这个圆的半径
area2 = float(input("请输入圆的面积: "))
r2 = math.sqrt(area2 / math.pi)
print("面积为", area2, '的圆的关径是:', r2)

