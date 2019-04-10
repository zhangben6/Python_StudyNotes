#   3. 输入一个正整数代表正方形的宽和高,打印如下正方形
#     如
#       请输入: 5
#     打印:
#       1 2 3 4 5
#       2 3 4 5 6
#       3 4 5 6 7
#       4 5 6 7 8
#       5 6 7 8 9
#     如
#       请输入: 3
#     打印:
#       1 2 3
#       2 3 4
#       3 4 5

n = int(input('请输入: '))

for line in range(1, n + 1):  # line 代表行数
    for i in range(line, line + n):
        print(i, end=' ')
    print()

