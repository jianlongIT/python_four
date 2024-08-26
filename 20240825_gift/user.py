# -*- coding: utf-8 -*-
# Auther : jianlong
from base import Base
from common import error
from common.utils import timestamp_to_string
import os, random
import multiprocessing


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        self.gift_random = range(1, 101)
        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        if self.username not in users:
            raise error.NotUserError('not user %s' % self.username)
        current_user = users.get(self.username)
        if not current_user.get('active'):
            raise error.UserActiveError('%s is not active' % self.username)

        if current_user.get('role') != 'normal':
            raise error.RoleError('%s is not normal' % self.username)

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get('create_time'))
        self.update_time = timestamp_to_string(current_user.get('update_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_list = []
        for level1, pool1 in gifts.items():
            for level2, pool2 in pool1.items():
                for k, v in pool2.items():
                    gift_list.append(v['name'])
        return gift_list

    def choice_gift(self, lock):
        with lock:
            self.get_user()
            first_num = random.choice(self.gift_random)
            if 1 <= first_num <= 50:
                first_level = 'level1'
            elif 51 <= first_num <= 80:
                first_level = 'level2'
            elif 81 <= first_num < 95:
                first_level = 'level3'
            elif first_num >= 95:
                first_level = 'level4'
            else:
                raise error.CountError('first_num %s is error' % first_num)
            gifts = self._Base__read_gifts()
            pool_one = gifts.get(first_level)
            second_num = random.choice(self.gift_random)
            if 1 <= second_num <= 50:
                second_level = 'level1'
            elif 51 <= second_num <= 80:
                second_level = 'level2'
            elif 81 <= second_num < 100:
                second_level = 'level3'
            else:
                raise error.CountError('second_num %s is error' % second_num)
            pool_two = pool_one.get(second_level)
            if len(pool_two) == 0:
                return
            gift_names = []
            for k, v in pool_two.items():
                gift_names.append(k)
            last_gift_name = random.choice(gift_names)
            gift_info = pool_two.get(last_gift_name)
            if gift_info is None or gift_info.get('count') == 0:
                return
            gift_info['count'] -= 1
            pool_two[last_gift_name] = gift_info
            pool_one[second_level] = pool_two
            gifts[first_level] = pool_one
            self.user.get('gifts').append(last_gift_name)
            self._Base__save(gifts, self.gift_json)
            self.update()
            print(last_gift_name)

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user
        self._Base__save(users, self.user_json)


if __name__ == '__main__':
    lock = multiprocessing.Lock()  # 创建一个进程锁
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    user = User('xiaoguo', user_path, gift_path)
    processes = [multiprocessing.Process(target=user.choice_gift, args=(lock,)) for _ in range(10)]
    for p in processes:
        p.start()

    for p in processes:
        p.join()
