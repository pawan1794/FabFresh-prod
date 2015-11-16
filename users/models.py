from django.db import models

class UserInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    addressLocality = models.CharField(max_length=255,blank=True,null=True)
    addressSubLocality = models.CharField(max_length=100, blank=True,null=True)
    addressLatitude = models.FloatField(blank=True,null=True)
    addressLogitude = models.FloatField(blank=True,null=True)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    flag = models.BooleanField(default=0, blank=True)


