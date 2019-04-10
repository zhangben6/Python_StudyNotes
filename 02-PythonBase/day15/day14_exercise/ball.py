#   1. 一个球从100米高空下落,每次落地后反弹高度为原高度
#     的一半,再落下,写程序:
#       1) 算出皮球在第10次落后反弹多高
#       2) 算出皮球在第10次反弹后经过多少米路程

def get_last_height(height, times):
    '''height 原来的代表高度
    times 代表需要反弹的次数'''
    for _ in range(times):
        height /= 2  # 算出一次反弹后的高度
    return height

print("第10次落下后反弹高度为:",
      get_last_height(100, 10), '米')

# 算出皮球在第10次反弹后经过多少米路程
def get_meter(height, times):
    '''height代表原始高度,
    times代表次数'''
    s = 0
    for _ in range(times):
        s += height  # 加上下落的高度
        height /= 2  # 算出本次反弹多高
        s += height  # 加上反弹高度
    return s

print("第10次反弹高经历的路程是",
      get_meter(100, 10), '米')