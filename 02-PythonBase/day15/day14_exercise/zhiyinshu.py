#   2. 分解质因数.输入一个正整数,分解质因数
#     如 输入: 90 则打印: 90=2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包括1))

# 分析:
#  输入90
# 第一步得到[2,3,3,5]
# 第二步再把上述列表转为字符串'2*3*3*5'

def get_zhiyin_list(n):
    '''如n 为 90
    返回 [2, 3, 3, 5]
    此函数用循环来实现
    '''
    L = []
    # 当 n大于1时,它一定有质因数
    while n > 1:
        # 1. 求一个质数因,放在L中
        for i in range(2, n + 1):
            if n % i == 0:  # i一定是质因数
                L.append(i)
                # 2. n缩小为 n = int(n / 质因数)
                n = int(n / i)
                break
    return L

def print_formula(n):
    L = get_zhiyin_list(n)  # [2, 3, 3, 5]
    L2 = [str(x) for x in L]  # ['2', '3', '3', '5']
    s = '*'.join(L2)  # 2*3*3*5
    print(n, '=', s)

print_formula(90)
print_formula(100)
# print(get_zhiyin_list(90))  # [2, 3, 3, 5]
# print(get_zhiyin_list(100))

