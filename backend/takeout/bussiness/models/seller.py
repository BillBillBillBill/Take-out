# coding: utf-8
# import sys
# sys.path.append("../..")
from lib.models.userbase import UserBase


class Seller(UserBase):
    # store_id = models.IntegerField(blank=True)

    def to_string(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
        }

    def get_store(self):
        try:
            return str(self.store.id)
        except:
            return ""

    def to_detail_string(self):
        return {
            "id": self.id,
            "store": self.get_store(),
            "username": self.username,
            "nickname": self.nickname,
        }

    class Meta(UserBase.Meta):
        db_table = 'seller'
