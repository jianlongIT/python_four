# -*- coding: utf-8 -*-
# Auther : jianlong
jine = float(input('请输入还款金额 : '))
qishu = int(input('请输入还款期数 : '))
huankuan = None
if qishu == 3:
    huankuan = (jine * 0.025) / 3
elif qishu == 6:
    huankuan = (jine * 0.045) / 6
elif qishu == 12:
    huankuan = (jine * 0.088) / 12
else:
    input('期数错误')

print('还款分为{}期 '.format(qishu), '每期还款额为:', huankuan)
