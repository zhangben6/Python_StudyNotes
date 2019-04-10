# function_embed_define.py

# 此示例示意在函数内部创建函数，在函数外部来调用内部的函数
# def fn_outer():
#     print("fn_outer被调用")

#     def fn_inner():
#         print("fn_inner被调用")

#     print("fn_outer调用结束")
#     return fn_inner  # 把fn_inner绑定的函数的引用关系返回

# fx = fn_outer()
# fx()


def fn_outer():
    print('函数fn_outer被调用')
    def fn_inner():
        print('函数fn_inner终于被调用了!!!')
    print('函数fn_outer调用结束。。。')
    return fn_inner
fx = fn_outer()
fx()