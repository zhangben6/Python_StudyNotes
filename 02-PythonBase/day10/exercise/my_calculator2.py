
def get_func(s):
    '''此函数功能是,传入一个字符串用s绑定,根据s的
    值返回上面相应的函数, 如s == '+'或 s=='加' 返回
    myadd
    '''
    def myadd(x, y):
        return x + y

    def mysub(x, y):
        return x - y

    def mymul(x, y):
        return x * y


    if s == '加' or s == '+':
        return myadd
    elif s == '减' or s == '-':
        return mysub
    elif s == '乘' or s == '*':
        return mymul

def main():
    while True:
        s = input("请输入计算公式: ") # 1 加 2
        L = s.split()  # L = ['1', '加', '2']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是:3

print(dir())
main()  # 调用主函数

