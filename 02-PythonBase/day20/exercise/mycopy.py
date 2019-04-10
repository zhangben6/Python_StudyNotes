#   1. 写程序实现复制文件的功能
#      要求:
#        1. 要考虑超大文件问题
#        2. 要能复制二进制文件(如:图片等)
#        3. 要考虑关闭文件

def copyfile(src_file, dst_file):
    '''src_file 源文件名
       dst_file 目标文件名'''
    try:
        with open(src_file, 'rb') as fr, open(dst_file, 'wb') as fw:
            while True:
                # 每次搬4096个字节
                data = fr.read(4096)
                if not data:  # 已到达文件尾
                    break
                fw.write(data)
            print("复制文件有成功")
    except OSError:
        print("复制失败")

src = input("请输入源文件:　")
dst = input("请输入目标文件: ")
copyfile(src, dst)

