from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, class_prepared
from users import MAX_USERNAME_LENGTH, REQUIRE_UNIQUE_EMAIL
from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext_lazy as _

class UserInfo(models.Model):
    owner = models.OneToOneField('auth.User', related_name='UserInfo')
    phone = models.CharField(max_length=10,unique=True)
    otp = models.IntegerField(blank=True,null=True)
    flag = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.owner)

class Wallet(models.Model):
    owner = models.OneToOneField('auth.User' , related_name='Wallet')
    wallet = models.FloatField(max_length=1000000,default=0)

def create_user_Info(sender, instance, created, **kwargs):
    if created:
        profile, created = UserInfo.objects.get_or_create(owner=instance)
        wallet, created = Wallet.objects.get_or_create(owner=instance)

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

def longer_username_and_email_signal(sender, *args, **kwargs):
    if (sender.__name__ == "User" and
        sender.__module__ == "django.contrib.auth.models"):
        patch_user_model_username(sender)
        patch_user_model_email(sender)
class_prepared.connect(longer_username_and_email_signal)

def patch_user_model_username(model):
    field = model._meta.get_field("username")
    field.max_length = MAX_USERNAME_LENGTH()
    field.help_text = _("Required, %s characters or fewer. Only letters, "
                        "numbers, and @, ., +, -, or _ "
                        "characters." % MAX_USERNAME_LENGTH())

    # patch model field validator because validator doesn't change if we change
    # max_length
    for v in field.validators:
        if isinstance(v, MaxLengthValidator):
            v.limit_value = MAX_USERNAME_LENGTH()


def patch_user_model_email(model):
    field = model._meta.get_field("email")
    field.blank = False
    field._unique = REQUIRE_UNIQUE_EMAIL()
    field.max_length = MAX_USERNAME_LENGTH()
    field.help_text = _("Required, %s characters or fewer. Only letters, "
                        "numbers, and @, ., +, -, or _ "
                        "characters." % MAX_USERNAME_LENGTH())
    # patch model field validator because validator doesn't change if we change
    # max_length
    for v in field.validators:
        if isinstance(v, MaxLengthValidator):
            v.limit_value = MAX_USERNAME_LENGTH()


if User._meta.get_field("email").max_length != MAX_USERNAME_LENGTH():
    patch_user_model_email(User)

if User._meta.get_field("username").max_length != MAX_USERNAME_LENGTH():
    patch_user_model_username(User)

class AndroidAppVersion(models.Model):
    versionNumber = models.FloatField()
    serverShutdown = models.BooleanField(default=False)
    serverShutdownReason = models.CharField(max_length=300,null=True)
    def __str__(self):
        return str(self.versionNumber)

class NotificationBoard(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    notification_valid_until_time = models.DateTimeField()

    def __str__(self):
        return self.title