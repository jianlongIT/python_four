# -*- coding: utf-8 -*-
# Auther : jianlong
import os

path = os.getcwd() + '/line.txt'
message = ['jianlong\n', 'ssss\n', 'aaaa\n']
f = open(path, 'a')
f.writelines(message)
f.close()
