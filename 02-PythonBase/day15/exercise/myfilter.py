# 1.试写一个生成器myfilter函数,此函数与系统内建的
#     filter函数功能一致

def myfilter(fn, iterable):
    for x in iterable:
        if fn(x):  # 用fn函数判断x是否符合条件
            yield x

for x in myfilter(lambda x: x % 2 == 1, range(10)):
    print(x)