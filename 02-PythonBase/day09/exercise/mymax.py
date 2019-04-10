#   已知内建函数 max 的绑助文档为:
#      max(...)
#        max(iterable)---> value
#        max(args1, arg2, *args)  --> value

#     仿造max函数，写一个与max功能完全一样的mymax函数
#     (要求: 不允许调用内键的max函数)
#     如:
#       def mymax(...):
#           ...
#       print(mymax([6, 8, 3, 5]))  # 8
#       print(mymax(100, 200))  # 200
#       print(mymax(1, 3, 5, 9, 7))  # 9
#       print(mymax())   # 报错
      
def mymax(a, *args):
    if len(args) == 0:  # 判断是否是一个参数:
        # 求可迭代对象的最大值:
        zuida = a[0]
        for x in a:
            if x > zuida:
                zuida = x
        return zuida
    else:
        zuida = a
        for x in args:
            if x > zuida:
                zuida = x
        return zuida
        
# print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
# print(mymax(1, 3, 5, 9, 7))  # 9
# print(mymax())   # 报错
      
