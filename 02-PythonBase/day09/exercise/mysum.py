# 练习:
#   写一个程序，mysum 可以传入任意个实参的参数，
#   此函数的功能是返回所有实参的和
#     def mysum(*args):
#         ....
#     print(mysum(1,2,3,4))  # 10
#     print(mysum(1,2,3))  # 6

def mysum(*args):
    '''在此函数内要实现求和算法'''
    s = 0  # 用来累加
    for x in args:
        s += x
    return s


print(mysum(1,2,3,4))  # 10
print(mysum(1,2,3))  # 6
