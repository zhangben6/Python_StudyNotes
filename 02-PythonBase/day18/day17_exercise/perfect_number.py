# 练习:
#   1. 完全数:
#     1 + 2 + 3 = 6  (6为完全数)
#     1, 2,3为都为6的因数(能被一个数x整除的数y,则y为
#          x的因数)
#     1 x 6 = 6
#     2 x 3 = 6
#     完全都是指除自身以外的所有因数之和相加等于自身的数
#     求4 - 5个完全数
#     答案:
#       6
#       28
#       496
#       ...

def is_perfect_number(x):
    '''此函数判断x是否是完全数
    如果是完全数返回True,否则返回False'''
    L = []  # 此列表用于存放 所有的因数
    for i in range(1, x):
        if x % i == 0:  # 是因数
            L.append(i)
    # 走到此步，所有的因数已存在于L中
    if sum(L) == x:
        return True
    return False

i = 1
while True:
    if is_perfect_number(i):
        print(i)
    i += 1

