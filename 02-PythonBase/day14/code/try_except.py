# try_except.py


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
    print("div_apple函数内部发生错误," + 
          "已处理,程序恢复正常状态")
except ZeroDivisionError:
    print("用户输的人数为0, 程序已恢复正常状态")
    print('没有人的取苹果,苹果被收回')

print("程序结束!")
