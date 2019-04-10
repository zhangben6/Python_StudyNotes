# class_variable.py

# 此示例示意类变量的定义，访问及赋值操作
class Human:
    total_count = 0  # 创建一个类变量

print("Human.total_count=", Human.total_count)
Human.total_count += 100
print(Human.total_count)  # 100

Human.class_var2 = 200  # 创建第二个类变量

print(dir(Human))