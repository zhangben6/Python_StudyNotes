
# 此示例示意 序列传参
def myfun(a, b, c):
    '''这是一个函数传参的示例'''
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)

L = [11, 22, 33]

# myfun(L[0], L[1], L[2])
myfun(*L)

# myfun(L)