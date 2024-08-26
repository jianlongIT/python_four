# -*- coding: utf-8 -*-
# Auther : jianlong
from base import Base
from common import error
import os


class Admin(Base):

    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user is None:
            raise error.NotUserError('not user %s' % self.username)

        if not current_user.get('active'):
            raise error.UserActiveError('%s is not active' % self.username)

        if current_user.get('role') != 'admin':
            raise error.RoleError('%s is not admin' % self.username)

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def __check(self):
        self.get_user()
        if self.role != 'admin':
            raise Exception('not permission')

    def add_user(self, username, role):
        self.__check()
        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        self.__check()
        self._Base__change_active(username=username)

    def update_user_role(self, username, role):
        self.__check()
        self._Base__change_role(username=username, role=role)

    def add_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        self._Base__write_gift(first_level=first_level, second_level=second_level, gift_name=gift_name,
                               gift_count=gift_count)

    def delete_gift(self, first_level, second_level, gift_name):
        self.__check()
        self._Base__delete_gift(first_level=first_level, second_level=second_level, gift_name=gift_name)

    def update_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        self._Base__gift_update(first_level=first_level, second_level=second_level, gift_name=gift_name,
                                gift_count=gift_count, is_admin=True)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    admin = Admin('jianlong', user_path, gift_path)
    admin.add_user(username='xiaoguo', role='admin')
    admin.update_user_role(username='xiaoguo', role='normal')
    # admin.update_gift('level1', 'level3', 'iPad', 100)
