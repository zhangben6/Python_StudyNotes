#   3. 计算三险一金：
#     已知社保的缴费比率是:
#      项目       个人缴费比例   单位缴费比例
#     养老保险       8%             19%
#     工伤保险       0%             0.5%
#     医疗保险      2%+3元          10%
#     住房公积金     12%            12%
#    输入您在北京的社保基数(如: 5000)
#      打印您和公司的个项缴费明细、个人总缴费金额、
#      单位缴费金额及国家拿到的钱是多少？

base = float(input("请输入社保基数: "))
yanglao_gr = base * 0.08
yanglao_dw = base * 0.19
gongshang_gr = 0
gongshang_dw = base * 0.005
yiliao_gr = base * 0.02 + 3
yiliao_dw = base * 0.1  # 10%
gongjijin_gr = base * 0.12
gongjijin_dw = base * 0.12

print('个人养老:', yanglao_gr)
print('单位养老:', yanglao_dw)
print('个人工伤:', gongshang_gr)
print('单位工伤:', gongshang_dw)
print('个人医疗:', yiliao_gr)
print('单位医疗:', yiliao_dw)
print('个人公积金:', gongjijin_gr)
print('单位公积金:', gongjijin_dw)

total_gr = yanglao_gr + gongshang_gr + \
           yiliao_gr + gongjijin_gr

total_dw = yanglao_dw + gongshang_dw + \
           yiliao_dw + gongjijin_dw

print("个人缴费总金额: ", total_gr)
print("单位缴费总金额: ", total_dw)

print("国家总收费金额: ", total_gr + total_dw)

