


def div_apple(n):
    print("%d个苹果想分给几个人?" % n)
    s = input("请输入人数: ")
    count = int(s)  # 可能触发ValueError错误
    result = n / count  # 可能触发ZeroDivisionErorr错误
    print("每个人分了", result, "个苹果")

try:
    div_apple(10)
    print("分苹果成功")
except (ValueError, ZeroDivisionError):
    print("苹果不分了")
# except ValueError:
#     print("苹果不分了")
# except ZeroDivisionError:
#     print("苹果不分了")


print("程序结束!")
