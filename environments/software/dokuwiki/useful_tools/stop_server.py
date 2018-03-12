#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20140829
#  @date
#  @version       0.0
#  @brief         stop dokuwiki Apache server
import os
import time
import signal
import subprocess

os.chdir(r'server')
print("Stop Apache Server")
p = subprocess.Popen(["ApacheKill.exe"])

### Replace "ApacheKill.exe" ###
# is_success_killed = False
# with open('apache_log.txt', 'r') as io_r:
#     pid = io_r.readline()
#     print(pid)
#     pid = int(pid)
#     if pid > 100:
#         os.kill(pid, signal.CTRL_C_EVENT)  # signal.SIGTERM
#         is_success_killed = True

# time.sleep(3)
# if is_success_killed:
#     os.remove("apache_log.txt")

print("It's Stopped")
time.sleep(3)
