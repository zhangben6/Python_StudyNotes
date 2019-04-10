#   已知有如下字符串的列表:
#     L = ['Tarena', 'XiaoZhang', 'xiaowang']
#   生成如下字典:
#     d = {'Tarena':6, 'XiaoZhang':9,
#           'xiaowang':8}


L = ['Tarena', 'XiaoZhang', 'xiaowang']
# 方法1, 用字典推导式
# d = {s: len(s) for s in L}

# 方法2, 用for语句实现
d = {}
for s in L:
    d[s] = len(s)

print(d)

# d = {'Tarena':6, 'XiaoZhang':9,
#       'xiaowang':8}
