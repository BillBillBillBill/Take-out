# coding: utf-8
from lib.models.userbase import UserBase
from lib.models.image import ImageStore


class Seller(UserBase):

    def to_string(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "account_type": self.get_account_type_display()
        }

    def get_store(self):
        try:
            return str(self.store.id)
        except:
            return ""

    def to_detail_string(self):
        data = {
            "id": self.id,
            "store": self.get_store(),
            "username": self.username,
            "nickname": self.nickname,
            "account_type": self.get_account_type_display()
        }
        if self.image_ids:
            data['images'] = ImageStore.get_by_ids(self.image_ids)
        else:
            data['images'] = []
        return data

    class Meta(UserBase.Meta):
        db_table = 'seller'
