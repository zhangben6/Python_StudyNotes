# 2. 分三次输入当前时间的小时，分钟，秒数
#     再计算出距离凌晨0:0:0过了多少秒

# h = int(input("请输入小时: "))
# m = int(input("请输入分钟: "))
# s = int(input("请输入秒:"))

# second = h * 60 * 60 + m * 60 + s
# print("距离0:0:0 已经过了", second, '秒')

# 反过来求时间
s = int(input("请输入秒:"))
h = s // 3600
m = (s - 3600 * h) // 60
s = s % 60
print(h,m,s)
