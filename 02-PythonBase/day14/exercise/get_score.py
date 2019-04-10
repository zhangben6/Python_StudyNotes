#   写一个函数 get_score() 来获取学生输入的成绩
#   信息(0-100)的整数,如果输入出现异常,则此函数返回0,
#   否则返回用户输入的成绩
#     def get_score():
#         ....  # 此处自己实现(try语句可以加在函数内部)

#     score = get_score()
#     print("学生的成绩是:", score)


def get_score():
    try:
        s = int(input("请输入成绩(0~100): "))
    except ValueError:
        s = 0  # 或者return 0
    # 如果s在[0,100]之间返回s
    if 0 <= s <= 100:
        return s
    # 如果s不在[0,100] 之间返回0
    return 0

score = get_score()
print("学生的成绩是:", score)