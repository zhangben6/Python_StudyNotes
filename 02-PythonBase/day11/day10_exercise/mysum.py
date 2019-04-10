#   1. 给出一个数n,写一个函数mysum来计算
#      1 + 2 + 3 + .... + n 的和
#     要求用函数来做
#     如:
#       print(mysum(100))  # 5050


# 方法1
# def mysum(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += i
#     return s

# 方法2
def mysum(n):
    return sum(range(1, n + 1))

print(mysum(100))  # 5050
print(mysum(10000))


