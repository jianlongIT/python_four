# -*- coding: utf-8 -*-
# Auther : jianlong
import os, json, time
from common import error
from common.utils import check_file, timestamp_to_string
from common.consts import ROLES, FISTLEVELS, SECONDLEVELS


class Base(object):
    def __init__(self, user_json, gift_json):
        self.gift_json = gift_json
        self.user_json = user_json
        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

    def __check_user_json(self):
        check_file(self.user_json)

    def __check_gift_json(self):
        check_file(self.gift_json)

    def __read_users(self, time_to_str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())
        if time_to_str == True:
            for username, v in data.items():
                v['create_time'] = timestamp_to_string(v['create_time'])
                v['update_time'] = timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    def __change_role(self, username, role):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        if role not in ROLES:
            raise error.RoleError('not use role %s' % role)
        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user
        self.__save(users, self.user_json)
        return True

    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        user['active'] = not user['active']
        user['update_time'] = time.time()

        users[username] = user
        self.__save(users, self.user_json)
        return True

    def __delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        delete_user = users.pop(username)
        self.__save(users, self.user_json)
        return delete_user

    def __write_user(self, **user):
        if 'username' not in user:
            raise ValueError('missing username')
        if 'role' not in user:
            raise ValueError('missing role')
        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_users()
        if user['username'] in users:
            raise error.UserExistsError('user %s has exists' % user['username'])
        users.update({
            user['username']: user
        })

        self.__save(users, self.user_json)

    def __read_gifts(self):
        with open(self.gift_json, 'r') as f:
            data = f.read()
            json_data = json.loads(data)
        return json_data

    def __init_gifts(self):
        data = {
            'level1': {
                'level1': {},
                'level2': {},
                'level3': {}
            }, 'level2': {
                'level1': {},
                'level2': {},
                'level3': {}
            }, 'level3': {
                'level1': {},
                'level2': {},
                'level3': {}
            }, 'level4': {
                'level1': {},
                'level2': {},
                'level3': {}
            }
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
            return
        else:
            gifts = data
        self.__save(gifts, self.gift_json)

    def __write_gift(self, first_level, second_level, gift_name, gift_count):
        get_data = self.__check_gifts(first_level, second_level, gift_name)
        gifts = get_data.get('gifts')
        second_pool = get_data.get('second_pool')
        first_pool = get_data.get('first_pool')
        if gift_count <= 0:
            gift_count = 1
        if gift_name in second_pool:
            second_pool[gift_name]['count'] += gift_count
        else:
            second_pool[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }
        first_pool[second_level] = second_pool
        gifts[first_level] = first_pool
        self.__save(gifts, self.gift_json)

    def __delete_gift(self, first_level, second_level, gift_name):
        get_data = self.__check_gifts(first_level, second_level, gift_name)
        gifts = get_data.get('gifts')
        second_pool = get_data.get('second_pool')
        first_pool = get_data.get('first_pool')

        if gift_name not in second_pool:
            return False
        delete_gift = second_pool.pop(gift_name)
        first_pool[second_level] = second_pool
        gifts[first_level] = first_pool
        self.__save(gifts, self.gift_json)
        return delete_gift

    def __check_gifts(self, first_level, second_level, gift_name):
        if first_level not in FISTLEVELS:
            raise error.LevelError('first_level not exists %s' % first_level)
        if second_level not in SECONDLEVELS:
            raise error.LevelError('second_level not exists %s' % second_level)
        gifts = self.__read_gifts()
        first_pool = gifts[first_level]
        second_pool = first_pool[second_level]
        return {
            'first_pool': first_pool,
            'second_pool': second_pool,
            'gifts': gifts
        }

    def __gift_update(self, first_level, second_level, gift_name, gift_count=1, is_admin=False):
        assert isinstance(gift_count, int), 'gift_count is a int'
        get_data = self.__check_gifts(first_level, second_level, gift_name)
        gifts = get_data.get('gifts')
        second_pool = get_data.get('second_pool')
        first_pool = get_data.get('first_pool')
        if gift_name not in second_pool:
            return False
        if is_admin:
            if gift_count <= 0:
                raise error.CountError('gift count cant be %d' % gift_count)
            second_pool[gift_name]['count'] = gift_count

        else:
            if gift_count > second_pool[gift_name]['count']:
                raise error.NegativeNumberError('gift count cant negative')
            second_pool[gift_name]['count'] -= gift_count
        first_pool[second_level] = second_pool
        gifts[first_level] = first_pool
        self.__save(gifts, self.gift_json)

    def __save(self, data, path):
        json_data = json.dumps(data)
        with open(path, 'w') as f:
            f.write(json_data)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    base = Base(user_path, gift_path)
    # base.write_user(username='jianlong',role='admin')
    # base.delete_user(username='jianlong2')
    # result = base.read_gifts()
    # print(result)
    # base.init_gifts()
    # base.delete_gift(first_level='level1', second_level='level1', gift_name='mac')
