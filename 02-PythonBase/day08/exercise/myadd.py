# 练习:
#   写一个函数myadd, 此函数中的参数列表里有两个参数x, y
#     此函数功能是打印 x + y 的和
#     def myadd(...):
#         ...
#     myadd(100, 200)   # 300
#     myadd("ABC", "123")  # ABC123



def myadd(x, y):
    z = x + y
    print(z)
    # print(x + y)

myadd(100, 200)   # 300
myadd("ABC", "123")  # ABC123

myadd([1, 2, 3], [4, 5, 6])
