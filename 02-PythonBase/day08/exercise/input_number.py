#   3. 写一个函数input_number
#       def input_number():
#           .... # 此处自己实现
#       此函数用来获取用户循环输入的整数,当输入负数时结束输入
#       将用户输入的数字以列表的形式返回,再用内建函数max,min,
#       sum 求出用户输入的数的最大值,最小值及和,如:
#       L = input_number()
#       print("最大数是:", max(L))
#       print("最小数是:", min(L))
#       print("和是:", sum(L))



def input_number():
    myl = []
    while True:
        n = int(input("请输入正整数: "))
        if n < 0:  # 负数退出循环
            break
        myl.append(n)
    return myl

L = input_number()
print(L)
# print("最大数是:", max(L))
# print("最小数是:", min(L))
# print("和是:", sum(L))
