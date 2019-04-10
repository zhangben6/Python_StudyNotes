# 输入一个数字，用程序来判断这个数是正数,
# 是负数还是零
# 以下两行可以改写为一行
# s = input("请输入一个数字: ")
# f = float(s)  # 转为浮点数
f = float(input("请输入一个数字: "))

# 开始判断
if f < 0:
    print(f, '是负数')
elif f > 0:
    print(f, '是正数')
# elif f == 0:
else:
    print(f, '是零')

