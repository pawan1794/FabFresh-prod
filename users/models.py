from django.db import models


class UserInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

