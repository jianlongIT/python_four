# -*- coding: utf-8 -*-
# Auther : jianlong

import os

path = os.getcwd()
print(path)
print(os.path.join(path, 'test'))
new_path = os.path.join(path, 'test/package')
print(os.path.split(new_path))
