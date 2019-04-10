#   3. 计算 BMI指数(Body Mass Index) 又称身体质量指数
#     计算公式:
#         BMI = 体重(公斤)/身高的平方(米)
#     如:一个69公斤的人，身高173公分，则
#        BMI = 69 / 1.73 ** 2  # 得23.05
#     标准表:
#       BMI < 18.5    体重过轻
#       18.5 <= BMI < 24  体重正常
#       BMI >= 24     体重过重
#     要求:  输入身高和体重，打印BMI的值，并打印体重状况

kg = float(input("请输入体重(公斤): "))
m = float(input("请输入身高(米): "))
bmi = kg / m ** 2
print("BMI =", bmi)

