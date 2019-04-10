# mymax.py

# 此示例示意定义一个带有形参的函数,并调用
def mymax(a, b):
    # 此函数将打印两个实参中的最大值:
    print("a =", a)
    print("b =", b)
    if a > b:
        print("最大值是:", a)
    else:
        print("最大值是:", b)

mymax(100, 200)
mymax("ABC", "123")


