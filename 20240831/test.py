# -*- coding: utf-8 -*-
# Auther : jianlong

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    smtpdobj = smtplib.SMTP()
    smtpdobj.connect('smtp.163.com', '25')
    smtpdobj.login('guojianlongit', 'TBSKZRYKMWJMDMKX')
    # message = MIMEText('<p style="color:red">python测试邮件不要from</p>', 'html', 'utf-8')
    # message['from'] = Header('guojianlongit@163.com')
    message = MIMEMultipart()
    message['Subject'] = Header('python脚本测试不要from', 'utf-8')
    attr = MIMEText(open('IMG_0326.JPG', 'rb').read(), 'base64', 'utf-8')
    attr['Content-Type'] = 'application/octet-stream'
    attr['Content-Disposition'] = 'attachment;filename="IMG_0326.JPG"'
    message.attach(attr)
    message.attach(MIMEText('这是一个带附件的邮件', 'plain', 'utf-8'))

    smtpdobj.sendmail('guojianlongit@163.com', ['328852120@qq.com'], message.as_string())
