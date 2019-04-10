# mynumber2.py


# 此示例示意int, float函数的重写方法

class MyNumber:
    def __init__(self, value):
        self.data = value

    def __int__(self):
        '''此方法用于将对象self.转为整数
        此方法必须返回整数
        '''
        return int(self.data)
    def __float__(self):
        return float(self.data)
    def __round__(self,k):
        return round(self.data,3)
n1 = MyNumber(2.313213)
print(int(n1))  # 调用n1.__int__()
print(float(n1))  # 调用n1.__float__()
print(round(n1,3))
