#   ３．　编写函数fun,其实能是计算下列多项式的和
#      Sn = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
#      建义用数学模块里的factorial
#      求n 等于500时的值

# 方法1
# def fun(n):
#     from math import factorial as fac

#     Sn = 0
#     for x in range(n + 1):
#         Sn += 1/fac(x)
#     return Sn

# 方法2
def fun(n):
    from math import factorial as fac
    Sn = sum(map(lambda x:1/fac(x), range(n + 1)))
    return Sn

print(fun(500))

