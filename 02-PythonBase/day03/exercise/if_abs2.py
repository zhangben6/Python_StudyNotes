#   2. 写一个程序，输入一个数，用条件表达式计算出这个数
#     的绝对值并打印出结果
n = int(input("请输入一个整数: "))

r = -n if n < 0 else n

print(n,'的绝对值是:', r)

