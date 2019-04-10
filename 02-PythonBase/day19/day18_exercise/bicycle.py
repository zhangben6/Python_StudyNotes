# 练习:
#   1. 写一个类Bicycle自行车类,有run方法,调用时
#   显示骑行的里程km
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
#     再写一个EBicycle电动自行车类,在Bicycle的基础
#     上添加了电池电量volume属性,有两个方法:
#       fill_charge(vol)  用来充电 vol为电量
#       run(km)  方法,每骑行10km消耗电量1度,同时显
#       示当前电量,当电量耗尽时则调用Bicycle的run方法
#       (用脚蹬骑行)
    
#     class EBicycle:
#         ....
#     b = EBicycle(5)  新买的电动车内有5度电
#     b.run(10) 电动骑行了10km里,还剩4度电
#     b.run(100) 电动骑行了40km里,还剩0度电,用脚蹬
#             骑行了60km
#     b.fill_charge(10)  电动自行车充电10度
#     b.run(50)  电动骑行了50km里,还剩5度电



class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, '公里')

class EBicycle(Bicycle):
    def __init__(self, vol=0):
        self.volume = vol  # 初始电量

    def run(self, km):
        # 如果有电就电动骑行，如果没电就用脚蹬骑行
        # 算出电动骑行的里程
        e_km = min(km, self.volume * 10)
        if e_km > 0:
            self.volume -= e_km / 10
            print("电动骑行了%d公里" % e_km,
            '剩余电量是:', self.volume, '度')
        if km > e_km:  # 说明电量不够电动骑行
            super().run(km - e_km)

    def fill_charge(self, vol):
        '''充电操作'''
        self.volume += vol      


b = EBicycle(5)  # 新买的电动车内有5度电
# b.run(10)  # 电动骑行了10km里,还剩4度电
b.run(100)  # 电动骑行了40km里,还剩0度电,用脚蹬
            # 骑行了60km
b.fill_charge(10)  # 电动自行车充电10度
b.run(50)  # 电动骑行了50km里,还剩5度电