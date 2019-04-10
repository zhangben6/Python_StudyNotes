#   1. 写一个程序，以电子时钟的格式打印时间：
#   　　格式:
#        HH:MM:SS
#       要求:每一秒钟变化一次　

import time

def clock():
    while True:  # 永不停止
        # 获取当前时间
        t = cur_time = time.localtime()
        # 显示
        # print("%02d:%02d:%02d" %
        #       (t[3], t[4], t[5]))
        print("%02d:%02d:%02d" % t[3:6],end='\r')
        time.sleep(1)


clock()
