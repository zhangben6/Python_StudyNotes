# file : mymod.py

'''这是自定义的模块的文档标题

这是模块的描述部分....
.... 此处省略200字
...
'''

def myfac(n):
    '''这是函数的文档字符串'''
    print("正在计算n的阶乘")

def mysum(n):
    print("!!!正在计算1 + 2 + 3 + .... + %d的和" % n)

name1 = "Audi"
name2 = "tesla"

print("mymod.py 文件被加载并导入")
print("当前我这个模块在:", __file__)
print("mymod.py模块的模块名为:", __name__)

if __name__ == '__main__':
    print("您正在用 python3 把 mymod.py当主模块运行")
else:
    print("此模块是被import 导入运行的")
