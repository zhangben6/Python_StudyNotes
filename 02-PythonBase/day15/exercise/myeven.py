# 练习:
#   写一个生成器函数myeven(start, stop) 用来生成从
#     start 开始,到stop结束(不包含 stop) 区间范围内
#     的一系列偶数

#     def myeven(start, stop):
#         ....  # 此处自己实现
#     evens = list(myeven(10, 20))
#     print(evens)  # [10, 12, 14, 16, 18]
#     for x in myeven(21, 30):
#        print(x)  # 打印 22 24 26 28


# 方法1 用while循环
# def myeven(start, stop):
#     i = start
#     while i < stop:
#         if i % 2 == 0:
#             yield i
#         i += 1

# 方法2, 用for循环
def myeven(start, stop):
    # 校正数据
    if start % 2 == 1:
        start += 1
    for i in range(start, stop, 2):
        yield i

# # 思考如下语句是在做什么:
# def myeven(start, stop):
#     if start % 2 == 1:
#         start += 1
#     return range(start, stop, 2)

# evens = list(myeven(10, 20))
# print(evens)  # [10, 12, 14, 16, 18]
for x in myeven(21, 30):
    print(x)  # 打印 22 24 26 28

def myeven(start,stop):
    if start % 2 == 1:
        start += 1
    for i in range(start,stop,2):
        yield i

    