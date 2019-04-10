#   2. 给出一个数n,写一个函数myfac来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * ... * n
#     print(myfac(5))  # 120

def myfac(n):
    s = 1
    for x in range(1, n + 1):
        s *= x
    return s



print(myfac(5))
print(myfac(4))
print(myfac(3))
print(myfac(2))
print(myfac(1))
print(myfac(100))
