
# 此示例示意try-except语句finally子句的作用

def div_apple(n):
    print("%d个苹果想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  # 可能触发ValueError错误
    result = n / count  # 可能触发ZeroDivisionErorr错误
    print("每个人分了", result, "个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except ValueError:  # 此处只捕获ValueErorr类型的错误
    print("出现异常,苹果不分了")
finally:
    # 此处的语句,只要离开此try语句,则此处的语句
    # 一定会被执行
    print("我是finally子句,我一定会被执行")

print("程序结束!")
