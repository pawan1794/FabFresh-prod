from django.contrib import admin
from models import UserInfo, UserProfile,PostalCode


class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('postalCode','Locality',)


# Register your models here.
admin.site.register(UserInfo)#, OrderAdmin)
admin.site.register(UserProfile)
admin.site.register(PostalCode,PostalCodeAdmin)
