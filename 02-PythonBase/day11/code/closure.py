# closure.py
# 什么是闭包
#   闭包是指引用了此函数外部变量的函数
#     (外部变量指:外部嵌套函数作用域内的变量)
# 闭包必须满足三个条件:
#     1. 必须有一个内嵌函数
#     2. 内嵌函数必须引用外部函数中的变量
#     3. 外部函数返回值必须是内嵌函数
# # 此示例示意闭包的定义及调用
# def make_power(y):
#     def fn(x):  # fn绑定一个闭包函数
#         return x ** y
#     return fn
# pow2 = make_power(2)  # pow2绑定一个闭包函数
# print("5的平方是:", pow2(5))

# pow3 = make_power(3)
# print("6的立方是:", pow3(6))

# 闭包的函数形式
def myfunc(y):
    def power(x):
        return x**y
    return power
result = myfunc(2)
print(result(6))