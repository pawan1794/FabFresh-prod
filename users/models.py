from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserInfo(models.Model):
    owner = models.OneToOneField('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10)

    def __unicode__(self):
        return unicode(self.owner)

def create_user_Info(sender, instance, created, **kwargs):
    if created:
       profile, created = UserInfo.objects.get_or_create(owner=instance)


post_save.connect(create_user_Info, sender=User)

class PostalCode(models.Model):
    postalCode = models.IntegerField(primary_key=True)
    Locality = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.postalCode)

class UserProfile(models.Model):

    owner = models.ForeignKey('auth.User', related_name='UserProfile')
    postalcode = models.ForeignKey('PostalCode',related_name='postalcode')
    address = models.CharField(max_length=255)
    addressLocality = models.CharField(max_length=255,blank=True,null=True)
    addressSubLocality = models.CharField(max_length=100, blank=True,null=True)
    addressLatitude = models.FloatField(blank=True,null=True)
    addressLogitude = models.FloatField(blank=True,null=True)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    flag = models.BooleanField(default=0, blank=True)

    def __str__(self):
        return "%s's Profile" % self.owner


'''def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
'''

