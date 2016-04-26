from django.db import models


class UserBase(models.Model):
    ACCOUNT_TYPES = (
        ("P", "Phone"),
        ("E", "Email")
    )
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    nickname = models.CharField(max_length=20)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True
