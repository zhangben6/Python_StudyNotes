# 2、中国古代的秤是16两1斤,请问现在的216两是古代
#    的几斤几两,写程序打印出来

jin = 216 / 10  # 现在的斤
# 算出古代的两
gudai_liang = jin * 16

# 算出古代的斤
gudai_jin = gudai_liang // 16

# 算出古代的两
gd_liang = gudai_liang % 16  # 求余
print("216两是古代的", gudai_jin, '斤',
            gd_liang, "两")




