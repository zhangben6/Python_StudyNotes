#   3. 给出一个数n,写一个函数计算:
#     1 + 2**2 + 3**3 + .... + n**n的和


def mysum(n):
    # 求: 1 + 2**2 + 3**3 + .... + n**n的和
    # 方法1
    # s = 0
    # for i in range(1, n + 1):
    #     s += i ** i
    # return s
    return sum(map(lambda x:x**x, range(1, n + 1)))


print(mysum(2))  # 5
print(mysum(3))  # 5
