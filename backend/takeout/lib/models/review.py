# coding: utf-8
from django.db import models
from bussiness.models.food import Food
from customer.models.orders import Order
from customer.models.customer import Customer
from bussiness.models.store import Store


class Review(models.Model):
    STAR_LEVEL = (
        ("1", "很差"),
        ("2", "差"),
        ("3", "一般"),
        ("4", "好"),
        ("5", "很好"),
    )
    content = models.CharField(max_length=200)
    star = models.CharField(max_length=1, choices=STAR_LEVEL)
    created_time = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def to_string(self):
        data = {
            "content": self.content,
            "star": self.get_start_display(),
            "created_time": self.created_time
        }
        return data


class FoodReview(Review):
    food = models.ForeignKey(Food, related_name='food_reviews')
    order = models.ForeignKey(Order, related_name='food_reviews')
    customer = models.ForeignKey(Customer, related_name='food_reviews')

    def to_string(self):
        data = super(FoodReview, self).to_string(self)
        data.update({
            "id": self.id,
            "food": self.food.id,
            "order": self.order.id,
            "customer": self.customer.id
        })
        return data


class OrderReview(Review):
    delivery_time = models.DateField()

    food = models.ForeignKey(Food, related_name='food_reviews')
    order = models.ForeignKey(Order, related_name='food_reviews')
    customer = models.ForeignKey(Customer, related_name='food_reviews')
    store = models.ForeignKey(Store, related_name='food_reviews')

    def to_string(self):
        data = super(OrderReview, self).to_string(self)
        data.update({
            "id": self.id,
            "food": self.food.id,
            "order": self.order.id,
            "customer": self.customer.id,
            "store": self.store.id,
        })
        return data
