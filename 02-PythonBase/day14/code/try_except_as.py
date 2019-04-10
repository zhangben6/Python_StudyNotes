

def div_apple(n):
    print("%d个苹果想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  # 可能触发ValueError错误
    result = n / count  # 可能触发ZeroDivisionErorr错误
    print("每个人分了", result, "个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except ValueError as err:
    # err绑定ValueError类型的错误对象
    # err 中存有错误信息
    # 在此处能否知道是用户输入的什么内容导致错误
    print("错误的起因是:", err)

print("程序结束!")
