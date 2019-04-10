# iterator.py

L = [2, 3, 5, 7]
# 1. 用for循环迭代访问:
for x in L:
    print(x)

print('-----------')
myit = iter(L)  # 从L中拿到迭代器,用myit来绑定
# while True:
#     try:
#         x = next(myit)  # 通过迭代器向L列表对象取数据
#         print(x)
#     except StopIteration:
#         break  #  结束循环,不再向迭代器获取数据


while 6:
    try:
        x = next(myit)
        print(x)
    except StopIteration:
        break
