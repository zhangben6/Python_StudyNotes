# func_give_func2.py

# 看如下程序的执行结果
def goodbye(L):
    for x in L:
        print("再见:", x)

def hello(L):
    for x in L:
        print("您好:", x)

names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def fx(fn, L):
    fn(L)

fx(hello, names)
fx(goodbye, names)
fx(hello, "ABC")  # hello("ABC")


