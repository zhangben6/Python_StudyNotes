# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 练习:
#   写一个程序,让用户输入很多个正整数,当输入小于零的数时
#   结束输入
#     1) 打印这些数中最大的数
#     2) 打印这些数中第二大的数
#     3) 删除最小的一个数

L = []  # 创建空列表容器准备存入数据
while True:
    n = int(input("请输入正整数: "))
    if n < 0:
        break
    L.append(n)  # L += [n]

print("L =", L)

# 1) 打印这些数中最大的数
zuida = max(L)
print("最大的数是:", zuida)
# 2) 打印这些数中第二大的数
#   1)先排序,找第二个元素
# L.sort()  # 排序后最后一个最大
# print("第二大的数是:", L[-2])
#   2) 把最大的全删除
L2 = L.copy()  # 复制一份
while zuida in L2:  # L内有最大数时就删除最大数
    L2.remove(zuida)
dierda = max(L2)
print("第二大是:", dierda)

# 3) 删除最小的一个数
zuixiao = min(L)
L.remove(zuixiao)  # 只删除一个
print("最后的列表为:", L)
