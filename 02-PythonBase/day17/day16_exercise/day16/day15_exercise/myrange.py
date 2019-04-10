#   1. 写一个生成器函数myxrange([start,]stop[,step])
#      来生成一系列的整数
#     要求myxrange功能与range函数功能完全相同
#     (不允许调用range函数和列表)
#     用自己写的myxrange,结合生成器表达式求 100以内所
#     有的奇数的平方和
def myxrange(start, stop=None, step=None):
    if step is None:
        step = 1
    if stop is None:
        stop = start
        start = 0
    if step > 0:
        while start < stop:
            yield start
            start += step
    if step < 0:  # 反向生成如:myxrange(10, 0, -3)
        while start > stop:
            yield start
            start += step



s = sum([x **2 for x in myxrange(100) if x % 2 == 1])
print(s)