# -*- coding: utf-8 -*-
# Auther : jianlong
import os
import pygame
import sys


def test(path):
    try:
        if os.path.isdir(path):
            list1 = os.listdir(path)
            for i in list1:
                new_path = path + '/' + i

                if os.path.isdir(new_path):
                    print(new_path)
                    test(new_path)
                else:
                    print(new_path)

    except PermissionError as e:
        print('---------')


test('/Users/dongzhiqiao')
