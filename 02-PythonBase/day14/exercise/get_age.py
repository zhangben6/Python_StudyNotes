# 练习:
#   写一个函数 get_age() 用来获取一个人的年龄信息
#   此函数的规定用户只能输入1~140之间的整数,如果用户
#   输入其它的数据则直接触发ValueError类型的错误通知
#   如:
#     def get_age():
#         ....
    
#     try:
#         age = get_age()
#         print("用户输入的年龄是:", age)
#     except ValueError as err:
#         print('用户输入的不是1~140之间的整数'
#               ',获取年龄失败')

# def get_age():
#     n = int(input("请输入年龄(1~140):"))
#     if n < 1 or n > 140:
#         raise ValueError("年龄不在规定的范围内!")
#     return n

# try:
#     age = get_age()
#     print("用户输入的年龄是:", age)
# except ValueError as err:
#     print('用户输入的不是1~140之间的整数'
#             ',获取年龄失败')
# 练习:
#   写一个函数 get_age() 用来获取一个人的年龄信息
#   此函数的规定用户只能输入1~140之间的整数,如果用户
#   输入其它的数据则直接触发ValueError类型的错误通知
#   如:
#     def get_age():
#         ....
    
#     try:
#         age = get_age()
#         print("用户输入的年龄是:", age)
#     except ValueError as err:
#         print('用户输入的不是1~140之间的整数'
#               ',获取年龄失败')
def get_age():
    try:
        n = int(input("请输入年龄1~140:"))
        if n < 1 or n > 140:
            raise ValueError(n," 不在指定范围内")
    finally:
        print("我是finally,我很顽强")
    return n
try:
    age = get_age()
    print('年龄是:',age)
except ValueError as err:
    print("您输入的数不在区间之内,错误的原因是:",err)
