from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

    def __unicode__(self):
        return unicode(self.owner)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return "%s's Profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)