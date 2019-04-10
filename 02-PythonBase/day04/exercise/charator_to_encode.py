# 1. 写一个程序，输入一段字符串，如果字符串不为空，则把第
#   一个字符的编码值打印出来

# x = input("请输入字符串: ")
# if x:
#     s = x[0]
#     print(chr(s))


# x = input("请输入字符串: ")
# if x != '':  # 等同于 if x:
#     c = x[0]  # 拿到第1个字符
#     print(c,'这个字符的编码值是:', ord(c))



#  5. 写一个myrange函数,参数可以传1~3个,实际含义
#     与range函数规则相同,此函数返回符合range函数规则
#     的列表
#     如:
#       L = myrange(4)
#       print(L)  # [0, 1, 2, 3]
#       L = myrange(4, 6)
#       print(L)  # [4, 5]
#       L = myrange(1, 10, 3)
#       print(L)  # [1, 4, 7]

def myrange(*args):
    L = []
    if len(args) == 1:
            i = 0
            while i < args[0]:
                L.append(i)
                i += 1
    if len(args) == 2:
        i = args[0]
        while i < args[1]:
            L.append(i)
            i += 1
    if len(args) ==3:
        i = args[0]
        while i < args[1]:
            L.append(i)
            i += args[2]
    return L
print(myrange(4))
L = myrange(4, 6)
print(L)
L = myrange(1, 10, 3)
print(L)
