

# 此示例示意用def语句来定义函数
def say_hello():
    a = 100
    print("内部a=", a)
    print("hello world")
    print("hello china")
    print("hello beijing")
    print("此函数外部的变量b=", b)
    # b = 1000  # 错,不能为全局变量赋值


b = 999  # 函数外部的全局变量
say_hello()
# print('a=', a)  # 出错
