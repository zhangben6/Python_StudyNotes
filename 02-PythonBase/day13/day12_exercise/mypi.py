#   4. 写程序求:
#      1/1 - 1/3 + 1/5 - 1/7 + 1/9 .. (+-)1/(2*n-1)
#      的和
#      　n最大数取 1000000
#     打印这个和
#     打印这个和乘以4的值(圆周率)

def get_value(n):
    s = 0
    sign = 1  # 用于代表符号 初始值为 正号
    for x in range(1, n + 1):
        s += sign* 1 / (2 * x - 1)
        # 变换符号
        sign *= -1

    return s

v = get_value(100000000)
print(v)
print(v * 4)

