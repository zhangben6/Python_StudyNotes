
# 此示例示意try-except语句else子句的作用

def div_apple(n):
    print("%d个苹果想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  # 可能触发ValueError错误
    result = n / count  # 可能触发ZeroDivisionErorr错误
    print("每个人分了", result, "个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except:
    print("出现异常,苹果不分了")
else:
    # 此处的语句只有在try中没有发生任何异常时才会执行
    print("没有出现异常,分苹果结束")

print("程序结束!")
