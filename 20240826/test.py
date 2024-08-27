# -*- coding: utf-8 -*-
# Auther : jianlong
import os, hashlib
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
                hash_content_obj = hashlib.md5(content.encode('utf-8'))
                hash_content = hash_content_obj.hexdigest()
            if file_name not in data:
                data[file_name] = {
                    p: hash_content
                }
            else:
                for k, v in data[file_name].items():
                    if v == hash_content:
                        is_delete = True
                        os.remove(p)
                    else:
                        is_delete = False
                if not is_delete:
                    data[file_name][p] = hash_content


if __name__ == '__main__':
    clear(os.getcwd())
