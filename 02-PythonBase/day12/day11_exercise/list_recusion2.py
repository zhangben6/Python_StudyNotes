#   2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有的数字
#        print_list(L)  # 打印 3 5 8 10 13...
#     2) 写一个函数sum_list(lst) 返回这个列表中所有数字
#        的和
#        print(sum_list(L))  # 106
#     注:
#       type(x) 可以返回一个变量的类型
#          如:
#            >>> type(20) is int  # True
#            >>> type([1, 2, 3, 4]) is list  # True


def print_list(lst, level=0):
    for x in lst:
        # 如果x是数字，则打印数字
        if type(x) is int:
            print(x, end=' ')
        # 如果x是列表，则再次打印x绑定的这个列表
        elif type(x) is list:
            print_list(x, level+1)
    if level == 0:
        print()  # 换行

L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

print_list(L)  # 打印 3 5 8 10 13...

# print(sum_list(L))  # 106

