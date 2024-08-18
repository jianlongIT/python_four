# -*- coding: utf-8 -*-
# Auther : jianlong
import os

path = os.getcwd()
f = open(path + '/test.txt', 'w')
f.write('hello jianlong')
f.close()

new_path = os.path.join(path, 'b.txt')
f = open(new_path, 'w')
f.write('hello , 鉴龙')
f.close()
f2 = open(new_path, 'w+')
f2.write(' yes')
f2.seek(0)
s = f2.read()
print(s)

new_path2 = os.path.join(path, 'c.txt')
f3 = open(new_path2, 'a+')
message = '1\n'
f3.write(message)
message_2 = '2\n'
f3.write(message_2)
f3.close()
