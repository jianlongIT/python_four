# -*- coding: utf-8 -*-
# Auther : jianlong

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        return 'X:{} , Y:{}'.format(self.x, self.y)


class Circle(Point):
    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    def string(self):
        print('该图形初始化点为：X：{}, Y：{}; 半径为：{}'.format(self.x, self.y, self.radius))


class Size(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def string(self):
        return 'Width：{}, Height：{}'.format(self.width, self.height)


class Rectangle(Point, Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            print(self.__dict__)
            self.__dict__[key] = value

    def string(self):
        point = Point.string(self)
        size = Size.string(self)
        print('该图形初始化点为{}'.format(point), end=' ')
        print('长宽分别为：{%s,%s}' % (self.width, self.height))


if __name__ == '__main__':
    rec = Rectangle(1, 2, 3, 4)
    rec.string()
    c = Circle(1, 2, 3)
    c.string()
    print(c.__dict__)
