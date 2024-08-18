# -*- coding: utf-8 -*-
# auther : jianlong

from datetime import datetime
from datetime import timedelta

now_time = datetime.now()
date = now_time.date()
time = now_time.time()
print(str(date))
print(str(time))
year_ = str(now_time.year)
month_ = str(now_time.month)
day_ = str(now_time.day)
print('{}-{}-{}'.format(year_, month_, day_))

new_str = '2019-09-10 8:10:56'
str_date = datetime.strptime(new_str, '%Y-%m-%d %H:%M:%S')
print(str_date)
now_ = datetime.now()
date_str = datetime.strftime(now_, '%Y/%m/%d %H:%M:%S')
print(date_str)

now_ = datetime.now()
print('now_', now_)
now_before = now_ - timedelta(days=3, hours=6, minutes=12)
now_after = now_ + timedelta(days=10)
print(now_before)
print(now_after)
