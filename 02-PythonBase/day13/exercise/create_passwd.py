# 练习:
#   用random模块,随机为自己生成一个6位数的数字密码
#      442260


def get_random_passwd():
    import random
    L = []  # 此列表用来绑定生成后的字符串列表
    s = '0123456789'
    for x in range(6):
        # 循环六次,每次从字符串s中随机取一个后放入L中
        ch = random.choice(s)
        L.append(ch)
    # print("L=", L)
    return ''.join(L)  # 返回字符串

passwd = get_random_passwd()
print("新生成的密码是:", passwd)

