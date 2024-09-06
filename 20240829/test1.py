# -*- coding: utf-8 -*-
# Auther : jianlong

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == '__main__':
    smtpdobj = smtplib.SMTP()
    smtpdobj.connect('smtp.163.com', '25')
    smtpdobj.login('guojianlongit', 'TBSKZRYKMWJMDMKX')
    message = MIMEText('python测试邮件不要from', 'plain', 'utf-8')
    # message['from'] = Header('guojianlongit@163.com')
    message['Subject'] = Header('python脚本测试不要from', 'utf-8')

    smtpdobj.sendmail('guojianlongit@163.com', ['328852120@qq.com'], message.as_string())
