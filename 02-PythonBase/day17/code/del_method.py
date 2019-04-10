# del_method.py


# 此示例示意析构方法的调用
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", info, '对象已经创建')
        # 打开文件

    def __del__(self):
        print("汽车", self.info, '对象即将销毁')
    

c1 = Car("BYD E6")
c2 = c1
del c1
input("请按回车键继续: ")