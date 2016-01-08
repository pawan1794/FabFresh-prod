from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
'''
STATUS = (
    ('0' , 'cancelled'),
    ('1', 'created'),
    ('2', 'wash'),
    ('3', 'dry'),
    ('4', 'iron'),
    ('5','processComplete'),
    ('6','shipRequest'),
    ('7','shipped'),
    ('8','completed')
)
'''

STATUS = (
    ('0', 'cancelled'),
    ('1', 'created'),
    ('2', 'pickup'),
    ('3', 'receivedAtCenter'),
    ('4', 'precheck'),
    ('5', 'tagging'),
    ('6', 'wash'),
    ('7', 'dry'),
    ('8', 'iron'),
    ('9', 'package'),
    ('10', 'shipped'),
    ('11', 'drop'),
    ('12', 'completed')
)

VALUETYPE = (
    ('0','percentage'),
    ('1','flat')
)

COUPONTYPE = (
    ('0','firstorder'),
    ('1','flatoff'),
    ('2','one time use')
)

LOGISTICS = (
    ('1','roadrunner'),
    ('2','shadowfax')
)

class CouponType(models.Model):
    coupon_type_id = models.AutoField(primary_key=True)
    coupon_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.coupon_type_name

class Coupon(models.Model):
    coupon_tag = models.CharField(max_length=100,unique=True)
    coupon_created_at_time = models.DateTimeField(auto_now_add=True)
    coupon_valid_until_time = models.DateTimeField()
    coupon_used_counter = models.IntegerField(blank=True,null=True)
    coupon_value_type = models.CharField(max_length=1,choices=VALUETYPE,default='1')
    coupon_value = models.IntegerField()
    coupon_valid_flag = models.BooleanField()
    coupon_coupon_type = models.CharField(max_length=1,choices=COUPONTYPE,default='1')
    #coupon_type = models.ForeignKey(CouponType,null=True)

    def __str__(self):
        return self.coupon_tag


class orders(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders')
    id = models.AutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at_time = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    status = models.CharField(max_length=2, choices=STATUS, default='1')
    order_type = models.CharField(max_length=10,blank=True,null=True)
    special_instructions = models.CharField(max_length=200,blank=True,null=True)
    p_id = models.IntegerField(blank=True,null=True)

    #Coupons
    coupon = models.ForeignKey(Coupon, blank=True,null=True)

    delivery_id = models.CharField(max_length=200, blank=True, null=True)
    roadrunner_order_id = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

class StatusTimeStamp(models.Model):
    order = models.ForeignKey(orders,related_name='StatusTimeStamp')
    status = models.CharField(max_length=2, choices=STATUS, default='1')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


class DriverDetails(models.Model):
    orders = models.ForeignKey(orders,related_name='DriverDetails')
    id = models.AutoField(primary_key=True)
    driver_phone = models.CharField(max_length=20,blank=True,null=True)
    order_id = models.CharField(max_length=20,blank=True,null=True)
    delivery_id = models.CharField(max_length=20,blank=True,null=True)
    new_trip = models.BooleanField(blank=True)
    driver_name = models.CharField(max_length=20,blank=True,null=True)
    logistics = models.CharField(max_length=1,choices=LOGISTICS,default=1)


#medium small or large
class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.size_name)

#shirt or pant
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100,unique=True)
    type_price_wash_and_iron = models.FloatField(max_length=100000,default=0.0, validators=[MinValueValidator(1)])
    type_price_wash = models.FloatField(max_length=100000,default=0.0, validators=[MinValueValidator(1)])
    type_price_iron = models.FloatField(max_length=100000,default=0.0, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return unicode(self.type_name)

#blue green etc
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=100)
    def __unicode__(self):
        return unicode(self.color_name)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    def __unicode__(self):
        return unicode(self.brand_name)

class ClothInfo(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(orders,related_name='ClothInfo')
    size = models.ForeignKey(Size)
    type = models.ForeignKey(Type)
    color = models.ForeignKey(Color)
    brand = models.ForeignKey(Brand,null=True)
    gender = models.CharField(max_length=7)
    damage = models.BooleanField(default=False)
