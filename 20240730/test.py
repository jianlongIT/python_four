# -*- coding: utf-8 -*-
# Auther : jianlong
try:
    print(name)
except (NameError,ZeroDivisionError) as e:
    print(e)
finally:
    print('finally')

