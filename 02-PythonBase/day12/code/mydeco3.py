# # mydeco.py

# # 此示例示意装饰器函数的定义方式及装饰器来装饰另一个函数
# # 的语法

# def mydeco(fn):
#     def fx():
#         print("++++++++++++++++")
#         fn()  # 调用以前的被装饰函数
#         print('----------------')
#     return fx   # 很灵性

# @mydeco
# def myfunc():
#     '''此函数将作为被装饰函数'''
#     print("myfunc被调用")
# myfunc = mydeco(myfunc)
# myfunc()
# # myfunc()
# # myfunc()


# 装饰器函数
def my_deco(fn):
    def fx():
        print('+++++++++++++')
        fn()
        print('-------------')
    return fx

@my_deco
def my_func():
    print('这是老函数')

# 原理
# func = my_deco(my_func)

#装饰函数
my_func()
