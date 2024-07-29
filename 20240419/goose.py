# -*- coding: utf-8 -*-
# Auther : jianlong
def goose(*args, **kwargs):
    i = 0
    name = '鹅，鹅，鹅，曲项向天歌，白毛浮绿水，红掌拨清波。'
    # 向控制台输出50个*号分隔符
    c = '*' * 50
    while i < 3:
        print(name)
        print(c)
        i += 1


# 调用函数实现效果
print(goose())


def test(*a, name, **b):
    print(name, a, b)


test(1, 's', 2, 5, 3, name='jianlong', age=12)


def test2(a, b, *args, **kwargs):
    print(a, b)
    print(args, kwargs)


test2(1, 2, *(1, 2), **{'name': 'jianlong'})

print(*(1, 2, 3))


def login(username, password):
    if username == 'imooc' and password == '123456':
        print('登录成功')
    else:
        print('登录失败')


login('a', 'b')
login('imooc', '123456')


def seq(num, num1, num2):
    if num < 88:
        return num1 * num2
    else:
        return num2 + num1


tuple1 = (5, 2, 1)
result = seq(*tuple1)
print(result)


def stu(name, age, major, country='CN'):
    print('jianlong')


stu('jianlong', 12, major='math', country='CN')
