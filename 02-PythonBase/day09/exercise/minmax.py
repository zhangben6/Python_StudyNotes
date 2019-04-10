#   写一个函数minmax,传入三个参数,返回这三个参数中的最大值和最
#   小值元素,结果要求,形成元组最小值在前,最大值在后返回
#   给调用者
#    如:
#       def minmax(a, b, c):
#           ....

#     调用结果如下:
#       t = minmax(300, 100, 200)
#       print(t)  # (100, 300)


def minmax(a, b, c):
    zd = a
    if b > zd:
        zd = b
    if c > zd:
        zd = c
    zx = min(a, b, c)
    return (zx, zd)

t = minmax(300, 100, 200)
print(t)  # (100, 300)

t2 = (1, 3, 2)
t3 = minmax(*t2)
print(t3)   # (1, 3)

