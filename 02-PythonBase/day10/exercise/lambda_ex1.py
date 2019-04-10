# 练习:
#   1. 写一个lambda表达式
#     fx = lambda n: .....
#   此表达式创建的函数判断n这个数的平方+1 能否被5整除,
#   如果能整除则返回True,否则返回False
#     print(fx(3))  # True
#     print(fx(4))  # False

# def fx(n):
#     if (n ** 2 + 1) % 5 == 0:
#         return True
#     return False

# def fx(n):
#     return True if (n ** 2 + 1) % 5 == 0 else False

# fx = lambda n: True if (n ** 2 + 1) % 5 == 0 else False
fx = lambda n: (n ** 2 + 1) % 5 == 0

print(fx(3))  # True
print(fx(4))  # False

