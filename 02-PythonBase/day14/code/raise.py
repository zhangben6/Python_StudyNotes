# raise.py

def make_except():
    print("开始....")
    # int('aaaa')  # 触发异常
    # ValueError是类型,故意触发一个异常
    # raise ValueError

    # e = ValueError("这是我故意制造的一个错误!")
    # raise e  # 发出错误通知,让程序进入异常状态
    raise ValueError("这是我故意制造的一个错误")
    # raise ZeroDivisionError("自定义的除零错误")

    print("结束!")

try:
    make_except()
except ValueError as err:
    print("得到make_except里发出的异常通知")
    print("err=", err)
except:
    print('错误了')

print("程序结束!")