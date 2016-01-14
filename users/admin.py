from django.contrib import admin
from models import UserInfo, UserProfile,PostalCode,Wallet,AndroidAppVersion,NotificationBoard


class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('postalCode','Locality',)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('owner','wallet',)


# Register your models here.
admin.site.register(UserInfo)#, OrderAdmin)
admin.site.register(UserProfile)
admin.site.register(PostalCode,PostalCodeAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(AndroidAppVersion)
admin.site.register(NotificationBoard)