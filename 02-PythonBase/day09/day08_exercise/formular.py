#   3. 编写函数,计算下列多项式的和:
#      Sn  = 1/(1*2) + 1/(2*3) + 1/(3*4) + ...
#          ... + 1/(n*(n+1))
#     def Sn(n):
#         ...
#     print(Sn(3))  # 0.75
#     print(Sn(1000))  # ???

def Sn(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (i * (i + 1))
    return s

print(Sn(3))  # 0.75
print(Sn(1000))  # ???

