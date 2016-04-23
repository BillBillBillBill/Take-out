# coding: utf-8
from django.db import models


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
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True, auto_now_add=True)
    owner = models.ForeignKey('seller', related_name='store')
