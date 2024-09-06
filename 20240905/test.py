# -*- coding: utf-8 -*-
# Auther : jianlong
from colorama import Back, Fore, Style

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    for index, value in enumerate(a):
        print(Fore.MAGENTA, index, value)
