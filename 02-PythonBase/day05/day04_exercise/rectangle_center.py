#   1. 输入三行文字，让这三行文字在一个方框 内居中显示
#   如输入:
#      hello!
#      I'm studing python!
#      I like python!
#   显示如下:
#      +---------------------+
#      |        hello!       |
#      | I'm studing python! |
#      |    I like python!   |
#      +---------------------+

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

zuida = len(a)
if len(b) > zuida:
    zuida = len(b)
if len(c) > zuida:
    zuida = len(c)

print("最长字符个数是: ", zuida)

line1 = '+' + '-' * (zuida + 2) + '+'
print(line1)
line2 = '| ' + a.center(zuida) + ' |'
print(line2)
print("| " + b.center(zuida) + ' |')
print("| " + c.center(zuida) + ' |')

print(line1)

