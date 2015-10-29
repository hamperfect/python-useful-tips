# -*- coding: utf-8 -*-

import os, time, subprocess
TERMINATE_PROGRAM = ["League of Legends.exe", "其他要关闭的程序.exe"]
# 可以写入多个想要关闭的程序
while True:
....for item in TERMINATE_PROGRAM:
........temp = 'taskkill /f /im "%s"' % item
........subprocess.Popen(temp, shell=True)
....time.sleep(1)

# 这个脚本的作用是定时关闭某一些程序，可改的参数有关闭的程序名和设定的时间
# 最后要放在系统里让他开机自行启动，路径：C:ProgramDataMicrosoftWindowsStart MenuProgramsStartUp
