#   1. 输入两个整数，分别用变量x，y绑定
#     1) 计算这两个数的和,并打印结果
#     2) 计算这两个数的积,并打印结果
#     3) 计算 x 的 y 次方是多少？并打印

x = int(input("请输入第一个数: "))
y = int(input("请输入第二个数: "))

# 1) 计算这两个数的和,并打印结果
print("两个数的和是: ", x + y)

# 2) 计算这两个数的积,并打印结果
z = x * y
print("两个数的积是: ", z)

# 3) 计算 x 的 y 次方是多少？并打印
print(x, '的', y, '次方是:', x ** y)

