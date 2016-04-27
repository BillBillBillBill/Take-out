# coding: utf-8
# import sys
# sys.path.append("../..")
from lib.models.userbase import UserBase
from lib.utils.password_tools import get_enc_password
from django.db import models


class Seller(UserBase):
    # store_id = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if self.created_time == self.updated_time:
            self.password = get_enc_password(self.password)
        super(Seller, self).save(*args, **kwargs)

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
