# -*- coding: utf-8 -*-
# Auther : jianlong
class Vehicle(object):
    def __init__(self, speed, size, trans_type='SUV'):
        self.speed = speed
        self.size = size
        self.trans_type = trans_type

    def show_info(self):
        last_size = self.size[0] * self.size[1] * self.size[2]
        print('该产品类型为{} 速度为{} 尺寸为{}'.format(self.trans_type, self.speed, last_size))

    def move(self):
        print('我已经向前移动了50米')

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_spped(self):
        print('我的时速为：设置的速度值{}km/h'.format(self.speed))

    def speed_up(self):
        old_speed = self.speed
        self.speed += 10
        print('我的时速由{}km/h 提升到了 {}km/h'.format(old_speed, self.speed))

    def speed_down(self):
        old_speed = self.speed
        self.speed -= 15
        print('我的时速由{}km/h 降低到了 {}km/h'.format(old_speed, self.speed))

    def transport_identify(self):
        if self.__class__.__name__ == 'Vehicle':
            print('类型匹配')
        else:
            print('类型不匹配')


if __name__ == "__main__":
    tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
    tool_1.set_speed(40)
    tool_1.show_info()
    tool_1.speed_up()
    tool_1.speed_down()
    tool_1.get_spped()
    tool_1.move()
    tool_1.transport_identify()
