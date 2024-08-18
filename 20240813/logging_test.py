# -*- coding: utf-8 -*-
# Auther : jianlong
import logging
import os


def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging


path = os.getcwd()
cus_path = os.path.join(path, 'back.log')

logging = init_log(cus_path)
logging.info('jianlong')
logging.warning('这是一个警告')
logging.error('这是一个错误')
logging.error('这是一个错误2')

