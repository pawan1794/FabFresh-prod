from django.contrib import admin
from models import UserInfo, UserProfile,PostalCode,Wallet,AndroidAppVersion,NotificationBoard,AllInOne,Car,Vehical


class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('postalCode','Locality',)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('owner','wallet',)
    list_filter = ['wallet' ]
    search_fields = ['wallet']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'addressLocality',)


class VehicalInline(admin.StackedInline):
      model = Vehical
      extra = 0


class CarAdmin(admin.ModelAdmin):
    inlines = [ VehicalInline, ]


# Register your models here.
admin.site.register(Car,CarAdmin)
admin.site.register(Vehical)
admin.site.register(AllInOne)
admin.site.register(UserInfo)#, OrderAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(PostalCode,PostalCodeAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(AndroidAppVersion)
admin.site.register(NotificationBoard)