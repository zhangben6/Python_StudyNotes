#   2. 看懂下列函数的输出结果是什么?为什么?
#     第1个程序
#     L = [2, 3, 5, 7]
#     a = [x*10 for x in L]
#     it = iter(a)
#     print(next(it))   # ???
#     L[1] = 333
#     print(next(it))   # ???
#     第2个程序
#     L = [2, 3, 5, 7]
#     a = (x*10 for x in L)
#     it = iter(a)
#     print(next(it))   # ???
#     L[1] = 333
#     print(next(it))   # ???


# 第1个程序
L = [2, 3, 5, 7]
a = [x*10 for x in L]
it = iter(a)
print(next(it))   # 20
L[1] = 333
print(next(it))   # 30

# 第2个程序
L = [2, 3, 5, 7]
a = (x*10 for x in L)
it = iter(a)
print(next(it))   # 20
L[1] = 333
print(next(it))   # 3330
