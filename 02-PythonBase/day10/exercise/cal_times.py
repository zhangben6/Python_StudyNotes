# 练习:
#   用全局变量记录一个函数hello 被调用的次数
#   部分代码如下:
#   count = 0
#   def hello(name):
#       print("你好", name)
#       ...  # 此处自己实现
#   hello("小张")
#   hello("小李)
#   print("hello函数共被调用", count, "次")  # 2


count = 0
def hello(name):
    print("你好", name)
    global count
    count += 1

hello("小张")
hello("小李")
print("hello函数共被调用", count, "次")  # 2
