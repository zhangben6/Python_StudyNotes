#   2. 写一个lambda 表达式来创建函数,此函数返回两个参
#     数的最大值
#     def mymax(x, y):
#          ....
#     mymax = lambda .....
#     print(mymax(100, 200))  # 200



def mymax(x, y):
    return x if x > y else y

mymax = lambda x, y: x if x > y else y

print(mymax(100, 200))  # 200
