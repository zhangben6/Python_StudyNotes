# staticmethod.py

# 此示例示意静态方法的定义的使用
class A:
    @staticmethod
    def myadd(a, b):
        return a + b

print(A.myadd(100, 200))  # 300 调用静态方法
a = A()
print(a.myadd(30, 40))  # 70

