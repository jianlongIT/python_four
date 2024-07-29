# -*- coding: utf-8 -*-
# Auther : jianlong

while True:
    print('欢迎使用货币转换系统')
    print('1、人民币转换美元')
    print('2、美元转换人民币')
    print('3、人民币转换欧元')
    print('0、结束程序')
    service = int(input('请选择您需要的服务'))
    if service == 1:
        print('欢迎使用人民币转换美元服务')
        jine = float(input('请输入您需要转换的人民币金额：'))
        print('您需要转换的人民币金额： {}元'.format(jine))
        dol = round(jine / 7.06, 2)
        print('兑换成美元为： {}元'.format(dol))
        continue
    if service == 0:
        print('感谢您的使用')
        break



