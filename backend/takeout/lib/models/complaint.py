# coding: utf-8
from django.db import models
from bussiness.models.store import Store
from customer.models.customer import Customer


# 投诉
class Complaint(models.Model):
    StatusList = (
        ("R", "Resolved"),
        ("I", "Ignored"),
        ("P", "Processing")
    )
    content = models.CharField(max_length=150)
    created_time = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=StatusList, default="P")
    store = models.ForeignKey(Store)
    customer = models.ForeignKey(Customer)

    def to_string(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_time": self.created_time,
            "store": self.store.name,
            "customer": self.customer.nickname,
            "status": self.get_status_display()
        }
