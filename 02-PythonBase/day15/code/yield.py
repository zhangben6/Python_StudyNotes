# yield.py


def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成结束")
r = myyield()
it = iter(r)   # 拿到生成器的迭代器
print(next(it))  # 2   向生成器获取数据
print(next(it))  # 3   向生成器获取数据
print(next(it))  # 5
print(next(it))  # 7
# print(next(it))  # StopIteration  通知生成结束
