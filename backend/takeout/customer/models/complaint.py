# coding: utf-8
from django.db import models
from bussiness.models.store import Store
from customer import Customer
from lib.utils.misc import get_timestamp_from_datetime


# 投诉
class Complaint(models.Model):
    StatusList = (
        ("R", "Resolved"),
        ("I", "Ignored"),
        ("P", "Processing")
    )
    content = models.CharField(max_length=150)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=StatusList, default="P")
    store = models.ForeignKey(Store, related_name='complaints')
    customer = models.ForeignKey(Customer, related_name='complaints')

    def to_string(self):
        data = {
            "id": self.id,
            "content": self.content,
            "created_time": get_timestamp_from_datetime(self.created_time),
            "store": self.store.name,
            "customer": self.customer.nickname,
            "status": self.get_status_display()
        }
        return data

    def to_detail_string(self):
        return self.to_string()
