# 练习:
#   1. 求:
#     1**2 + 2**2 +3**2 +...+9**2的和
#   2. 求:
#     1**3 + 2**3 +3**3 +...+9**3的和
#   3. 求:
#     1**9 + 2**8 + 3**7 + ... + 9**1的和

# 1**2 + 2**2 +3**2 +...+9**2的和
# 方法1
# def power2(x):
#     return x ** 2

# s = 0
# for x in map(power2, range(1, 10)):
#     s += x

# print("和是:", s)

# 方法2
def power2(x):
    return x ** 2
s = sum(map(power2, range(1, 10)))
print("和是:", s)

# 方法3
s = sum(map(lambda x:x**2, range(1, 10)))
print("和是:", s)

# 1**3 + 2**3 +3**3 +...+9**3的和
s = sum(map(lambda x:x**3, range(1, 10)))
print("和是:", s)

# 1**9 + 2**8 + 3**7 + ... + 9**1的和
# pow(x, y, z=None)
s = sum(map(pow, range(1, 10), range(9, 0, -1)))
print("第三题的和是:", s)


