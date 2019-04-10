
def myyield():
    yield 2
    yield 3
    yield 5
    yield 7

gen = myyield()
for x in gen:
    print(x)

print('----------')
# 生成器对象是一次性的,
# 一但生成生结束,将不能再重新生成数据
for x in gen:
    print(x)
print("====================")
for x in myyield():
    print(x)
print('--------------------')
for x in myyield():
    print(x)
