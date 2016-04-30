# coding: utf-8
from lib.models.userbase import UserBase


class Customer(UserBase):
    def to_string(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
        }

    def to_detail_string(self):
        return self.to_string()

    class Meta(UserBase.Meta):
        db_table = 'customer'
