from django.contrib import admin

from .models import orders,DriverDetails,Size, Type, Color, ClothInfo, Brand , StatusTimeStamp, Coupon, CouponType

class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner','id','amount' , 'quantity' , 'weight' , 'created_at_time','modified_at_time' ,'status', 'special_instructions','p_id')

class DriverDetailsAdmin(admin.ModelAdmin):
    list_display = ('orders','id','driver_name','new_trip','delivery_id','order_id','driver_phone')

class sizeAdmin(admin.ModelAdmin):
    list_display = ('size_id','size_name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_id','type_name')

class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_id' , 'color_name')

class ClothInfoAdmin(admin.ModelAdmin):
    list_display = ('cloth_id','order','size','type','color','gender')

class BrandInfoAdmin(admin.ModelAdmin):
    list_display = ('brand_id' , 'brand_name')

class StatusTimeStampAdmin(admin.ModelAdmin):
    list_display = ('order','status','timestamp')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_tag','coupon_created_at_time','coupon_valid_until_time','coupon_value_type','coupon_value','coupon_coupon_type','coupon_valid_flag')

admin.site.register(orders, OrderAdmin)
admin.site.register(DriverDetails, DriverDetailsAdmin)
admin.site.register(Size,sizeAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(ClothInfo,ClothInfoAdmin)
admin.site.register(Brand,BrandInfoAdmin)
admin.site.register(StatusTimeStamp,StatusTimeStampAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(CouponType)
admin.site.site_header = 'FabFresh'