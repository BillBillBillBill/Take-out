# coding: utf-8
# import sys
# sys.path.append("../..")
from lib.models.userbase import UserBase
from lib.utils.password_tools import get_enc_password
from django.db import models


class Seller(UserBase):
    store_id = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.created_time == self.updated_time:
            self.password = get_enc_password(self.password)
        super(Seller, self).save(*args, **kwargs)

    class Meta(UserBase.Meta):
        db_table = 'seller'
