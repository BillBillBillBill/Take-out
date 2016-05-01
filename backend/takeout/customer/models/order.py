# coding: utf-8
from django.db import models
from customer import Customer, DeliveryInformation
from bussiness.models.store import Store
from bussiness.models.food import Food
from lib.utils.misc import get_timestamp_from_datetime


class Order(models.Model):
    STATUS_LIST = (
        ("1", "未处理"),
        ("2", "已接单"),
        ("3", "配送中"),
        ("4", "已完成"),
        ("5", "已关闭"),
    )
    status = models.CharField(max_length=1, choices=STATUS_LIST, default="1")
    note = models.CharField(max_length=200, null=True)
    make_order_time = models.DateTimeField(auto_now_add=True)
    accept_order_time = models.DateTimeField(null=True)
    confirm_time = models.DateTimeField(null=True)
    total_price = models.FloatField()
    store = models.ForeignKey(Store, related_name='orders')
    customer = models.ForeignKey(Customer, related_name='orders')
    delivery_information = models.ForeignKey(DeliveryInformation, related_name='orders')

    def to_string(self):
        data = {
            "id": self.id,
            "status": self.get_status_display(),
            "note": self.note,
            "make_order_time": get_timestamp_from_datetime(self.make_order_time),
            "accept_order_time": get_timestamp_from_datetime(self.accept_order_time),
            "confirm_time": get_timestamp_from_datetime(self.confirm_time),
            "total_price": self.total_price,
            "store": self.store.id,
            "customer": self.customer.id,
        }
        data["food_list"] = [food.to_string() for food in self.order_foods.all()]
        return data

    def to_detail_string(self):
        return self.to_string()


class OrderFood(models.Model):
    count = models.IntegerField()
    order = models.ForeignKey(Order, related_name='order_foods', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='order_foods')

    def to_string(self):
        return {
            "id": self.id,
            "count": self.count,
            "order": self.order.id,
            "food": self.food.id
        }

    def to_detail_string(self):
        return self.to_string()
