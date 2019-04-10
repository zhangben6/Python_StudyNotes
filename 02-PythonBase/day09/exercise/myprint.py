  
# 思考:
#   print()　函数的形参列表是如何定义的

# def myprint(*args, sep=' ', end='\n', flush=False):
#     flag = False
#     for x in args:
#         if flag:  # 第二次及以后进入循环
#             print(sep, end='')
#         flag = True
#         print(x, end='')
#     print(end, end='')

# def myprint(*args, sep=' ', end='\n', flush=False):
#     print(*args, sep=sep, end=end)

# print()
# print(1, 2, 3, 4)
# print(1, 2, 3, 4, sep='#')
# print(1, 2, 3, 4, end='')

def my_print(*args,sep=' ',end='\n',flush=False):
    print(*args,sep=sep,end=end)
my_print(1,2,3,sep='')

