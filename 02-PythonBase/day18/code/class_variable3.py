# class_variable.py

# 此示例示意类变量的定义，访问及赋值操作
class Human:
    total_count = 0  # 创建一个类变量

h1 = Human()  # 创建一个实例
print("Human.total_count=", Human.total_count)  # 0
h1.total_count += 100  # 创建实例变量total_count
print(Human.total_count)  # 0
h1.__class__.total_count = 200
print(h1.total_count)  # 100  # 优先访问实例变量
print(Human.total_count)  # 200


