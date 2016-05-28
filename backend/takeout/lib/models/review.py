# coding: utf-8
from django.db import models
from bussiness.models.food import Food
from customer.models.order import Order
from customer.models.customer import Customer
from bussiness.models.store import Store
from lib.utils.misc import get_timestamp_from_datetime


class Review(models.Model):
    STAR_LEVEL = (
        ("1", "很差"),
        ("2", "差"),
        ("3", "一般"),
        ("4", "好"),
        ("5", "很好"),
    )
    content = models.CharField(max_length=200, null=True)
    star = models.CharField(max_length=1, choices=STAR_LEVEL, default="5")
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def to_string(self):
        data = {
            "content": self.content,
            "star": int(self.star),
            "created_time": get_timestamp_from_datetime(self.created_time)
        }
        return data


class FoodReview(Review):
    food = models.ForeignKey(Food, related_name='food_reviews')
    order = models.ForeignKey(Order, related_name='food_reviews')
    customer = models.ForeignKey(Customer, related_name='food_reviews')

    def to_string(self):
        data = super(FoodReview, self).to_string()
        data.update({
            "id": self.id,
            "food": self.food.id,
            "order": self.order.id,
            "customer": self.customer.id
        })
        return data


class OrderReview(Review):
    delivery_time = models.IntegerField(default=120)

    order = models.ForeignKey(Order, related_name='order_reviews')
    customer = models.ForeignKey(Customer, related_name='order_reviews')
    store = models.ForeignKey(Store, related_name='order_reviews')

    def to_string(self):
        data = super(OrderReview, self).to_string()
        data.update({
            "id": self.id,
            "order": self.order.id,
            "customer": self.customer.id,
            "store": self.store.id,
        })
        return data
