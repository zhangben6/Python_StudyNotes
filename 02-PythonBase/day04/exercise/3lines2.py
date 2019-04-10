#   输入三行文字，让这三行文字依次以20个字符的宽度右对齐
#     显示
#   如:
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行: aaaaaaa
#   打印结果如下:
#              hello world
#                     abcd
#                  aaaaaaa
#   做完上题后再思考：
#       能否以最长的字符串的长度进行右对齐显示（左侧填充
#       空格)

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

x = len(a)
y = len(b)
z = len(c)

# 求最大:方法1
# if x > y:
#     if x > z:
#         zhuida = x
#     else:
#         zhuida = z
# else:
#     if y > z:
#         zhuida = y
#     else:
#         zhuida = z

# 方法2
zhuida = x
if y > zhuida:
    zhuida = y
if z > zhuida:
    zhuida = z

print("最大值是: ", zhuida)

print(' ' * (zhuida - x) + a)
print(' ' * (zhuida - y) + b)
print(' ' * (zhuida - z) + c)

print('---------------------')
fmt = "%" + str(zhuida) + "s"
print('fmt=', fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)


