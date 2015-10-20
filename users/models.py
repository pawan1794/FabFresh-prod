from django.db import models


class UserInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    flag = models.BooleanField(default=0,blank=True)


