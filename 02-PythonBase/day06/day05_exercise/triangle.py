#   1.输入一个整数n,此整数代表三角形的直角边长
#      根据整数n打印如下四种三角形
#        请输入: 3
#     打印如下:
#       1)
#         *
#         **
#         ***
#       2)
#           *
#          **
#         ***
#       3)
#         ***
#         **
#         *
#       4)
#         ***
#          **
#           *


n = int(input("请输入:"))  # 假设为3

for line in range(1, n + 1):  # 表示当前行
    print("*" * line)
#   1)
#     *
#     **
#     ***
print()  # 空行

for line in range(1, n + 1):  # 行号
    blank = n - line  # 计算空格的个数
    print(" " * blank + '*' * line)
#   2)
#       *
#      **
#     ***
print()

for stars in range(n, 0, -1):
    print('*' * stars)

#   3)
#     ***
#     **
#     *
print()
for stars in range(n, 0, -1):
    blank = n - stars
    print(' ' * blank + '*' * stars)

#   4)
#     ***
#      **
#       *
