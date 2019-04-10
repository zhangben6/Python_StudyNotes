# mynumber.py


# 此示例示意让自定义的类能够使用内建函数进行操作
class Number:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print('__str__被调用')
        return "数字: %d" % self.data

    def __repr__(self):
        print("__repr__被调用")
        return 'Number(%d)' % self.data

n1 = Number(100)

print("repr(n1)=", repr(n1))  #n1.__repr__()
print("str(n1)= ", str(n1))  #n1.__str__()
print(n1)  # n1.__str__()
n2 = Number(200)
