# class_variable.py

# 此示例示意类变量的定义，访问及赋值操作
class Human:
    total_count = 0  # 创建一个类变量

h1 = Human()  # 创建一个实例

# 类变量可以通过类的实例直接访问(取值)
print(h1.total_count)  # 0  # 访问类变量

# h1.total_count = 100  # 此条语句是创建实例变量
# print(h1.total_count)  # 100
print("Human.total_count=", Human.total_count)  # 100?
print(dir(h1))


