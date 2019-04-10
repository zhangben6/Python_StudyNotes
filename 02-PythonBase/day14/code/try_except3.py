

def div_apple(n):
    print("%d个苹果想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  # 可能触发ValueError错误
    result = n / count  # 可能触发ZeroDivisionErorr错误
    print("每个人分了", result, "个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except ValueError:
    print("苹果不分了")
except:
    # 此处能够捕获除ValueErorr以外的全部错误
    print("except 子句被执行, 程序已转为正常状态!")
    # 注:  except: 子句只能写在所有except之后

print("程序结束!")
