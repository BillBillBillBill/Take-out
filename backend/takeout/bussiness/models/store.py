# coding: utf-8
from django.db import models
from bussiness.models.seller import Seller
from lib.models.image import ImageStore
from lib.utils.misc import get_timestamp_from_datetime


class Store(models.Model):
    BAN_STATUS = (
        ("Y", "yes"),
        ("N", "no")
    )
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    announcement = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_banned = models.CharField(max_length=1, choices=BAN_STATUS, default="N")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    image_ids = models.CharField(max_length=500, null=True)
    owner = models.OneToOneField(Seller, related_name='store')

    def to_string(self):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "announcement": self.announcement,
            "description": self.description,
            "owner": self.owner.to_detail_string(),
            "order_review_list": []
        }
        total_star = 0
        all_order_reviews = self.order_reviews.all()
        for order_review in all_order_reviews:
            order_review = order_review.to_string()
            data['order_review_list'].append(order_review)
            total_star += order_review.get("star", 5)
        order_reviews_length = len(all_order_reviews)
        if order_reviews_length != 0:
            data["average_star"] = total_star / float(len(all_order_reviews))
        else:
            data["average_star"] = 5
        data["total_orders_num"] = len(self.orders.all())
        if self.image_ids:
            data['images'] = ImageStore.get_by_ids(self.image_ids)
        else:
            data['images'] = []
        return data

    def to_detail_string(self):
        return self.to_string()
