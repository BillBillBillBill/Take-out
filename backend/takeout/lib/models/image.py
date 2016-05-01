# coding: utf-8
from django.db import models
from takeout.settings import STATIC_URL


class ImageStore(models.Model):
    name = models.CharField(max_length=150,null=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d')

    def to_string(self):
        path = STATIC_URL + self.img.path
        return {
            "name": self.name,
            "path": path
        }

    # 返回所有id的图片信息，id_str为逗号分割的id字符串
    @classmethod
    def get_by_ids(cls, id_str):
        id_list = id_str.replace(" ", "").split(",")
        ret_list = []
        for id in id_list:
            try:
                image = ImageStore.objects.get(id=id)
                ret_list.append(image.to_string())
            except Exception, e:
                print e.message
        return ret_list
