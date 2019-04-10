
# 练习 :
#   写一个程序,输入你的出生日期
#     1) 算出你已经出生了多少天?
#     2) 算出你出生那天是星期几?

import time  # 导入时间模块

y = int(input("请输入您出生的年: "))
m = int(input("请输入您出生的月: "))
d = int(input("请输入您出生的日: "))

# 形成元组
t = (y, m, d, 0, 0, 0, 0, 0, 0)
# 算出出生时新纪元的秒数
birth_time = time.mktime(t)

# 得到当前新纪元的秒数
current_time = time.time()
# 算出出生了多少秒
second = current_time - birth_time
# 算出出生的天数:
days = second / 60 / 60 / 24
print("您已出生%f天" % days)


# t = (1997,12,26,0,0,0,0,0,0)
# s1 = time.mktime(t)
# s2 = time.time()
# s3 = s2 - s1
# day = s3 // 3600*24



t2 = time.localtime(birth_time)
w = t2[6]

d = {
    0: "一",
    1: "二",
    2: "三",
    3: "四",
    4: "五",
    5: "六",
    6: "日",
}

print("您出生时是星期:", d[w])  # 0代表周一


