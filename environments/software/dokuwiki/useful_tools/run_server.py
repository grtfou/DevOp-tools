#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20140829
#  @date
#  @version       0.0
#  @brief         run dokuwiki Apache server
import os
import time
import subprocess
import webbrowser

os.chdir(r'server')
print("Start Apache Server")
cmd = ["mapache.exe"]
with open('apache_log.txt', 'w') as io_err:
    p = subprocess.Popen(cmd, stdout=io_err,
                              stderr=io_err, creationflags=8)
    io_err.write(str(p.pid)+ '\n')
print("It's Started")

# Open Browser
if os.path.isfile("..\dokuwiki\conf\local.php"):
    webbrowser.open('http://localhost:8800')
else:
    webbrowser.open('http://localhost:8800/install.php')

time.sleep(2)