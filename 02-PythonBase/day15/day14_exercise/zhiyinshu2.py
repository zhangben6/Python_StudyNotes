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
    此函数用 递归 来实现
    思路:
       1.   n <= 1 ,没有质因数 []
       2.   n > 1  至少有一个质因数
    '''
    if n <= 1:
        return []

    # 1. 求一个质数因
    for i in range(2, n + 1):
        if n % i == 0:  # i一定是质因数
            r = [i] + get_zhiyin_list(
                   int(n / i))
            return r

def print_formula(n):
    L = get_zhiyin_list(n)  # [2, 3, 3, 5]
    L2 = [str(x) for x in L]  # ['2', '3', '3', '5']
    s = '*'.join(L2)  # 2*3*3*5
    print(n, '=', s)

print_formula(90)
print_formula(100)
# print(get_zhiyin_list(90))  # [2, 3, 3, 5]
# print(get_zhiyin_list(100))

