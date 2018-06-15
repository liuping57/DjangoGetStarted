# coding: utf-8
from django.db import models


class UserMessage(models.Model):
    object_id = models.CharField(default="", max_length=50, primary_key=True, verbose_name="主键")
    name = models.CharField(null=True, blank=True, max_length=20, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="联系地址")
    message = models.CharField(max_length=500, verbose_name="留言消息")

    class Meta:
        verbose_name = '用户留言信息'



# Create your models here.
