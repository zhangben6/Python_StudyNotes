# 练习:
#   写一个函数,myadd,此函数可以传入二个,三个或四个实参
#     此函数功能是计算所有实参的和
#   如:
#     def myadd(...):
#         ....
#     print(myadd(10, 20))  # 30
#     print(myadd(100, 200, 300))  # 600
#     print(myadd(1, 2, 3, 4))  # 10



# def myadd(a, b, c=0, d=0):
#     return a + b + c + d

def myadd(a, b, c=None, d=None):
    if c is None:
        c = 0
    if d is None:
        d = 0
    return a + b + c + d

print(myadd(10, 20))  # 30
print(myadd(100, 200, 300))  # 600
print(myadd(1, 2, 3, 4))  # 10

