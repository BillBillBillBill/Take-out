# coding: utf-8
from django.db import models


class ImageStore(models.Model):
    name = models.CharField(max_length=150,null=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d')

