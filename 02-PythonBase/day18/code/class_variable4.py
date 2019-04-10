# class_variable.py

# 此示例示意类变量的定义，访问及应用
class Human:
    total_count = 0  # 创建一个类变量
    def __init__(self):
        print("__init__被调用")
        self.__class__.total_count += 1

    def __del__(self):
        self.__class__.total_count -= 1

h1 = Human()  # 创建一个实例
L = []
L.append(Human())
L.append(Human())
L.append(Human)
del h1
del L
print("当前共有", Human.total_count, '个对象')

print(dir())  # 当前全局变量只有Human


