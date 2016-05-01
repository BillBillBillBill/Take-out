# coding: utf-8
from django.db import models
from bussiness.models.store import Store
from lib.models.image import ImageStore
from lib.utils.misc import get_timestamp_from_datetime


class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    image_ids = models.CharField(max_length=500, null=True)
    store = models.ForeignKey(Store, related_name='foods', on_delete=models.CASCADE)

    def to_string(self):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }
        if self.image_ids:
            data['images'] = ImageStore.get_by_ids(self.image_ids)
        else:
            data['images'] = []
        return data

    def to_detail_string(self):
        data = self.to_string()
        data["store"] = self.store.id
        return data
