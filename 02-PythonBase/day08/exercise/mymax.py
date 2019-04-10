# 练习:
#   1. 写一个函数 mymax, 实现返回三个数的最大值:
#     如:
#         def mymax(a, b, c):
#             ...
#         print(mymax(100, 200, 300))  # 300
#         print(mymax("ABC", 'abc', '123'))  # abc


# 方法1
# def mymax(a, b, c):
#     z = a  # z用来绑定最大数
#     if b > z:
#         z = b
#     if c > z:
#         z = c
#     return z

# 方法2
def mymax(a, b, c):
    z = max(a, b, c)
    return z

# 方法3
def mymax2(x, y):
    # 返回两个数的最大值
    if x > y:
        return x
    return y

def mymax(a, b, c):
    return mymax2(mymax2(a, b), c)



print(mymax(100, 200, 300))  # 300
print(mymax("ABC", 'abc', '123'))  # abc

