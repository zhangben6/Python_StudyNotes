# star_tuple_args.py


# 此示例示意星号元组形参
def func(*args):
    print("实参的个数是:", len(args))
    print("args=", args)
func()  # 无参
# func(1,2,3,4)
func(1, 2, 3, 4, 5, 6, 7, 8)
# s = "ABCDE"
# func(*s)  # 等同于func('A', 'B', ....)


形参为*args　那么传入数据后里面的对象args是一个可迭代对象(元组)
