# raise2.py


# 此示例示意raise的语法
def f1(x):
    print(x)
    # 此处对x进行处理,可能触发错误
    e =  ValueError(str(x) + "此数值不能被处理")
    raise e
    # return e

def f2(x, y):
    try:
        f1(x)
    except ValueError as err:
        print("f1函数内部有错误产生,已处理", err)
        # raise err
        raise ZeroDivisionError
    print(x, y)

try:
    f2(0, 100)
except ValueError as err:
    print("f2函数内发生错误,已处理!!", err)
except:
    print('哈哈哈')

