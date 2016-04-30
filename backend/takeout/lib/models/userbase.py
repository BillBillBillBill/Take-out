from django.db import models
from lib.utils.password_tools import get_enc_password


class UserBase(models.Model):
    ACCOUNT_TYPES = (
        ("P", "Phone"),
        ("E", "Email")
    )
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPES)
    nickname = models.CharField(max_length=20)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.created_time == self.updated_time:
            self.password = get_enc_password(self.password)
        super(UserBase, self).save(*args, **kwargs)
