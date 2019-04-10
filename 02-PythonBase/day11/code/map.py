# def power2(x):
#     print("power2被调用, x=", x)
#     return x ** 2

# # 生成一个可迭代对象,此可迭代对象可以生成1~9的
# # 整数的平方
# for x in map(power2, range(1, 0)):
#     print(x)



def pow1(x):
    return x**2


for x in map(pow1,range(1,5)):
    print(x)