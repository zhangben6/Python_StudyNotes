
#  2. 写一个函数isprime(x) 判断x是否为素数.如果为素数
#     返回True,否则返回False
#     如:
#       print(isprime(3))  # True
#       print(isprime(4))  # False
    
#  3. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束
#     范围内的全部素数的列表,并打印对应的列表 (不包含n)
#     如:
#       def prime_m2n(m, n):
#            ...
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]
#  4. 写一个函数primes(n)  返回指定范围内的全部素数
#     (不包含n)的列表,打印印这些素数的列表, 如:
#       def primes(n):
#           ...
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#     1) 打印 100以内的素数
#     2) 打印 200以内全部素数的和





def isprime(x):
    if x < 2:
        return False
    # 此处x一定大于等于2
    for i in range(2, x):
        if x % i == 0:  # 整除就一定不是素数
            return False
    return True  # 走到此处x一定为素数

print(isprime(3))  # True
print(isprime(4))  # False


# 方法1
# def prime_m2n(m, n):
#     L = []
#     for x in range(m, n):
#         # 如果x是素数,把x放到列表中
#         if isprime(x):
#             L.append(x)
#     return L
# 方法2
def prime_m2n(m, n):
    return [x for x in range(m ,n) if isprime(x)]

L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


def primes(n):
    return prime_m2n(0, n)


L = primes(10)
print(L)  # [2, 3, 5, 7]
# 1) 打印 100以内的素数
print(primes(100))
# 2) 打印 200以内全部素数的和
s = sum(primes(200))
print("和是:", s)


