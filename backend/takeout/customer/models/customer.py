# coding: utf-8
from lib.models.userbase import UserBase
from django.db import models
from lib.models.image import ImageStore


class Customer(UserBase):
    def to_string(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "account_type": self.get_account_type_display()
        }

    def to_detail_string(self):
        data = self.to_string()
        if self.image_ids:
            data['images'] = ImageStore.get_by_ids(self.image_ids)
        else:
            data['images'] = []
        return data

    class Meta(UserBase.Meta):
        db_table = 'customer'


# 联系方式
class DeliveryInformation(models.Model):
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    receiver = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer)

    def to_string(self):
        data = {
            "id": self.id,
            "address": self.address,
            "phone": self.phone,
            "receiver": self.receiver,
            "customer": self.customer.id
        }
        return data
