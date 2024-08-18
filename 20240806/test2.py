# -*- coding: utf-8 -*-
# Auther : jianlong

import time
from datetime import datetime

now = time.time()
print('时间戳', now)

time_obj = time.localtime()
print(time_obj, '------')
time_str = time.strftime('%Y-%m-%d', time_obj)
time_obj_1 = time.strptime(time_str, '%Y-%m-%d')
print(time_obj_1)
print(datetime.now().timestamp())
