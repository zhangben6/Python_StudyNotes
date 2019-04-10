
# 此示例示意浅拷贝的过程和可能引发的问题

L = [3.1, 3.2]
L1 = [1, 2, L]
L2 = L1.copy()  # 浅拷贝
print(L1)  # ???
print(L2)  # ???
L2[2][0] = 3.14
print(L1)  # ???
print(L2)  # ???
print("L=", L)