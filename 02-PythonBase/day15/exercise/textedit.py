# 练习:
#   写一个程序,读入任意行文字,当输入空行时结束输入,
#   打印带有行号的输入结果
#   如:
#     请输入: hello<回车>
#     请输入: abc<回车>
#     请输入: tarena<回车>
#     请输入: <回车>
#   打印如下:
#     第1行: hello
#     第2行: abc
#     第3行: tarena

def input_text():
    L = []  # 此列表用于保存用户输入的字符串
    while True:
        s = input("请输入: ")
        if not s:
            break
        L.append(s)
    return L

def print_text(L):
    # 方法1
    # i = 1
    # while i <= len(L):
    #     print("第%d行:%s" % (i, L[i-1]))
    #     i += 1
    # 方法2
    for t in enumerate(L, 1):
        print("第%d行:%s" % t)


texts = input_text()
print_text(texts)
#     第1行: hello
#     第2行: abc
#     第3行: tarena
