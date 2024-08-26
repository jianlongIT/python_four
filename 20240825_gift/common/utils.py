# -*- coding: utf-8 -*-
# Auther : jianlong
import os
from . import error
from datetime import datetime


def check_file(path):
    if not os.path.exists(path):
        raise error.NotPathError('not found %s' % path)
    if not path.endswith('.json'):
        raise error.FormatError('need json format')
    if not os.path.isfile(path):
        raise error.NotFileError()


def timestamp_to_string(timestamp):
    formatted_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time
