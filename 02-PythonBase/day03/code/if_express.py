# if_express.py

# 此示例示意条件表达式的语法和用法
# 商场促销,满100 减 20
money = int(input("请输入商品总额: "))

# 计算需要支付金额
pay = money - 20 if money >= 100 else money
# 如果money >= 100 为True,相当于 pay=money-20
# 如果money >= 100 为False,相当于pay=money

print("您需要支付:", pay, "元")

