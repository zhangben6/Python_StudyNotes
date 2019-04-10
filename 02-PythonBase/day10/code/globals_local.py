# globals_local.py
# 此示例示意globals() 和 locals() 函数的用法
a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    print("local() 返回", locals())
    print("global() 返回:", globals())
    print(a, b, c, d, e)  # 1, 2, 100, 200, 300
    x = globals()
    print("全局变量c的值是:", x['c'])
    # print("全局变量c的值是:", globals()['c'])
fn(100, 200)
