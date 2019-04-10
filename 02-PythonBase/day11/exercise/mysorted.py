# 练习:
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据是:
#            'moT'   'yrreJ'  'ekipS'  'ekyT'
#   结果: ['Spike', 'Tyke', 'Tom', 'Jerry']


names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 排序的依据是:
#     'moT'   'yrreJ'  'ekipS'  'ekyT'
def myk(x):
    return x[::-1]  # 反回反转后的字符作为排序依据

L = sorted(names, key=myk)
print(L)
# 结果: ['Spike', 'Tyke', 'Tom', 'Jerry']