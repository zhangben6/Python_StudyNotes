#   1. 写一个函数 get_chinese_char_count(s),此函数的
#    功能是给定一个字符串,返回这个字符串中中文字符的个数
#    如:
#     def get_chinese_char_count(s):
#         ...
#     s = input("请输入中文英混合的字符串:")
#     print('您输入的中文个数是',
#            get_chinese_char_count(s))
#     注: 中文字符的编码在 0x4E00-0x9FA5 之间


def get_chinese_char_count(s):
    count = 0  # 记录中文字符的个数
    for ch in s:
        if 0x4e00 <= ord(ch) <= 0x9fa5:
            count += 1
    return count

s = input("请输入中文英混合的字符串:")
print('您输入的中文个数是',
        get_chinese_char_count(s))

# 注: 中文字符的编码在 0x4E00-0x9FA5 之间
