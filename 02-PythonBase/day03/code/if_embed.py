# if_embed.py


# 此示例示意if语句嵌套到另一个if语句内部
# 用嵌套实现输入月份判断季节

month = int(input("请输入月份(1～12): "))

if 1 <= month <= 12:
    print("输入正确")
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您的输入有误")

