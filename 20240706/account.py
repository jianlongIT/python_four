# -*- coding: utf-8 -*-
# Auther : jianlong
class Account(object):
    def __init__(self, j_time, bizhong, yue, zhaiyao=None, money=0):
        self.j_time = j_time
        self.zhaiyao = zhaiyao
        self.money = money
        self.bizhong = bizhong
        self.yue = yue

    def __show_info(self):
        print('交易日期{}  摘要 {}  金额{}  币种{}  余额{}'
              .format(self.j_time, self.zhaiyao, self.money, self.bizhong, self.yue))

    def add_money(self, add_money, zhaiyao):
        self.money = add_money
        self.yue += self.money
        self.zhaiyao = zhaiyao
        print('存入{}'.format(self.money))
        self.__show_info()


jianlong = Account('2024-07-08', '$', 10000.00)
jianlong.add_money(20.00, '转入')
jianlong.add_money(200000.00, '转入')
