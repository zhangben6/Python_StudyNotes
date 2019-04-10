#   2. 编写一个闹钟程序，启动时设置定时时间，到时间后
#     打印一句，时间到，然后退出程序

def alarm(h, m):
    import time
    while True:
        # 得到当前时间:
        t = time.localtime()
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        # if t[3] == h and t[4] == m:
        if t[3:5] == (h, m):
            print()  # 换行
            print("时间到...")
            return
        time.sleep(1)


hour = int(input('请输入小时: '))
minute = int(input('请输入分钟: '))
alarm(hour, minute)

