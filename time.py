import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("时间到！")
            # 播放提示音
            winsound.Beep(1000, 2000)
            break
        time.sleep(1)

# 设置闹钟时间
alarm_time = input("请输入闹钟时间（格式为HH:MM:SS）：")

# 启动闹钟
set_alarm(alarm_time)
