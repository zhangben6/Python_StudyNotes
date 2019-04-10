# 3. 打印杨辉三角(只打印6层, 思考题,明天或后天才讲)
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# 1 5 10 10 5 1

def get_next_line(L):
    '''L代表当前一行
    返回当前行的下一行
    如: L = [1, 2, 1]

    返回   [1, 3, 3, 1]
    '''
    # 最左侧加一个1
    rl = [1]  # 准备要返回的列表
    # 中间 加 len(L)-1个数
    for i in range(len(L)-1):
        rl.append(L[i] + L[i + 1])
    # 最右侧加一个1
    rl.append(1)
    return rl

def get_yanhui_list(n):  # n代表行数
    '''返回: [
        [1],
        [1, 1],
        [1, 2, 1],
        ...
    ]'''
    rl = []  # 此列表用于返回
    line = [1]  # 当前要处理的一行
    for _ in range(n):
        rl.append(line)  # 把当前行放进去
        line = get_next_line(line)
    return rl

def get_yanghui_string(L):
    ''' 如果L = [[1], [1, 1], [1, 2, 1]]
    返回rl = ["1", "1 1", "1 2 1"]
    '''
    rl = []
    for line in L:
        # 把 line=[1, 2, 1] 转为line=['1', '2', '1']
        line = [str(x) for x in line]
        s = ' '.join(line)
        rl.append(s)
    return rl

def print_yanghui_triangle(n):
    # 打印n行的杨辉三解
    L = get_yanhui_list(n)
    SL = get_yanghui_string(L)  # 字符串列表
    # 求最大长度:
    max_len = len(SL[-1])
    for line in SL:
        print(line.center(max_len))


print_yanghui_triangle(10)


# 测试函数
# L = get_yanhui_list(6)
# print(get_yanghui_string(L))
# # print(get_next_line([1]))