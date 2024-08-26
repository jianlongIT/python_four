# -*- coding: utf-8 -*-
# Auther : jianlong
import os
from glob import glob

data = {}


def clear(path):
    result = glob(path + '/*')
    for p in result:
        if os.path.isdir(p):
            clear(p)
        else:
            file_name = os.path.split(p)[-1]
            is_delete = True
            with open(p, 'r')as f:
                content = f.read()
            if file_name not in data:
                data[file_name] = {
                    p: content
                }
            else:
                for k, v in data[file_name].items():
                    if v == content:
                        is_delete = True
                        os.remove(p)
                    else:
                        is_delete = False
                if not is_delete:
                    data[file_name][p] = content


if __name__ == '__main__':
    clear(os.getcwd())
