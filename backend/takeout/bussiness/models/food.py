# coding: utf-8
from django.db import models
from bussiness.models.store import Store

class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True, auto_now_add=True)
    store = models.ForeignKey(Store, related_name='foods', on_delete=models.CASCADE)

    def to_string(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }

    def to_detail_string(self):
        data = self.to_string()
        data["store"] = self.store.id
        return data
