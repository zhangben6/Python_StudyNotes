# 练习:
#   试用递归方式实现
#     1 + 2 + 3 + 4 + .... + n 的和
#     如:
#       def mysum(n):
#          ....
#       print(mysum(100))  # 5050
#       print(mysum(10000))  # ???


def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)

print(mysum(100))  # 5050
print(mysum(10000))  # ???

