#   写一个程序,让用户分两次输入一个人的信息:
#      信息包含:  姓名 和 电话号码
#     让用户多个人的信息,当输入姓名为空时结束输入
#     把用户输入的数据存于字典中
#       姓名作为键, 电话号码作为值
#     最后打印存储数据的字典
#     如:
#       请输入姓名: 小张
#       请输入电话: 13888888888
#       请输入姓名: 小李
#       请输入电话: 13999999999
#       请输入姓名: <回车>
#     打印:
#       {"小张": 13888888888, "小李": 13999999999}

book = dict()  # book = {}  创建一个字典容器
while True:
    n = input('请输入姓名: ')
    if not n:
        break  # 退出循环
    a = int(input("请输入电话号码: "))
    book[n] = a

print(book)



